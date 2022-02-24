from urllib.error import HTTPError
import fire
import configparser
import threading
import time
from tqdm.auto import tqdm
from odiogarpa.models import Comment
import queue
from odiogarpa.database import get_db
from odiogarpa.preprocessing import preprocess_comment
from perspective import PerspectiveAPI

config = configparser.ConfigParser()

config.read("config.ini")

api_key = "AIzaSyDs6NtRRxaFupgtpdcfDG9BdvQLEH6_VM0" #Era: config["Perspective"]["API_KEY"]

def analyze_comments(num_comments=None, num_workers=10, sleep_time=0.1):
    print("Connecting to db")
    db = get_db()
    comments = Comment.select().where(
        Comment.was_processed == False
    )

    if num_comments is not None:
        comments = comments.limit(num_comments)

    print(f"{comments.count()} comments to analyze")
    print(config["Perspective"]["API_KEY"])

    q = queue.Queue()
    for comment in tqdm(comments):
        q.put(comment.id)

    def worker(timeout=1):
        db = get_db()
        perspective = PerspectiveAPI(api_key)
        while True:

            comment_id = q.get()
            comment = Comment.select().where(Comment.id == comment_id).get()

            current_sleep = 1

            while True:
                try:
                    text = comment.text
                    preprocessed_text = preprocess_comment(text)

                    ret = perspective.analyze_comment(
                        preprocessed_text,
                        languages=["es"],
                        requested_attributes={
                            "TOXICITY":{}, 
                            "SEVERE_TOXICITY":{}, 
                            "IDENTITY_ATTACK_EXPERIMENTAL": {},
                            "PROFANITY_EXPERIMENTAL": {},
                            "THREAT_EXPERIMENTAL": {},
                            "INSULT_EXPERIMENTAL": {}
                            })
                            
                    print("="*80)
                    print(ret)
                    toxicity = ret["attributeScores"]["TOXICITY"]["summaryScore"]["value"]
                    time.sleep(sleep_time)

                    comment.was_processed = True
                    comment.toxicity = toxicity
                    comment.preprocessed_text = preprocessed_text
                    comment.json_response = json.dumps(ret)

                    comment.save()

                    print(f"Comment updated: {preprocessed_text} --> TOXICITY: {comment.toxicity}")
                    print("="*80)
                    q.task_done()
                    break
                except HTTPError as e:
                    print("Error analyzing")
                    print(e.read())
                    print(f"Sleeping and retrying {current_sleep}")
                    time.sleep(current_sleep)
                    current_sleep = current_sleep * 2


    print(f"Creating {num_workers} workers")
    threads = []
    for _ in range(num_workers):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()
        threads.append(t)

    q.join()
    print("All threads joined")



if __name__ == "__main__":
    fire.Fire(analyze_comments)
