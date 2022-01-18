import fire
import pandas as pd
from tqdm.auto import tqdm
from odiogarpa.models import Comment
from odiogarpa.database import get_db


def load_db(path_to_csv, limit=None):
    print(f"Cargando datos de {path_to_csv}")
    df = pd.read_csv(path_to_csv)

    print(f"Cargando {len(df)} comentarios")
    print(f"Conectando con bbdd")
    db = get_db()
    db.connect()
    db.create_tables([Comment])

    print("Cargando comentarios")

    for index, row in tqdm(df.iterrows(), total=len(df)):
        comment = Comment(
            text=row['text'],
            youtube_id=row['id'],
        )
        comment.save()

        if index == limit:
            break


if __name__ == "__main__":
    """
    Uso google fire, que convierte una función en algo fácil de llamar desde consola
    https://github.com/google/python-fire
    """
    fire.Fire(load_db)