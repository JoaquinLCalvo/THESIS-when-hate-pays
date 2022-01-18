from peewee import *
from .database import get_db

class Comment(Model):
    text = TextField()
    preprocessed_text = TextField(default="")
    youtube_id = CharField(max_length=50)
    toxicity = FloatField(null=True)
    was_processed = BooleanField(default=False)
    class Meta:
        database = get_db()
