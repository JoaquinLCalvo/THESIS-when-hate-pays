from peewee import *
from .database import get_db

class Comment(Model):
    text = TextField()
    preprocessed_text = TextField(default="")
    youtube_id = CharField(max_length=50)
    toxicity = FloatField(null=True)
    json_response = TextField(default="")
    was_processed = BooleanField(default=False, index=True)
    class Meta:
        database = get_db()
