import fire
import configparser
import threading
from tqdm.auto import tqdm
from odiogarpa.models import Comment
import queue
from odiogarpa.database import get_db
from odiogarpa.preprocessing import preprocess_text
from perspective import PerspectiveAPI

config = configparser.ConfigParser()

config.read("config.ini")

api_key = config["Perspective"]["API_KEY"]

def analyze_comments(num_comments=None, num_workers=10):
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

            toxicity = perspective.analyze(comment.text)

            q.task_done()

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