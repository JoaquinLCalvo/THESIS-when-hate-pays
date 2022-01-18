import os
from pathlib import Path
from peewee import *

project_path = Path(__file__).parent.parent

db_path = os.path.join(project_path, 'comments.db')
print(db_path)
_db = SqliteDatabase(db_path)

def get_db():
    return _db