from src.DataBase import BaseModel
from src.models.user import User
from datetime import datetime
import peewee

class Message(BaseModel):
    text = peewee.TextField()
    user_a = peewee.ForeignKeyField(User)
    user_b = peewee.ForeignKeyField(User)

    createdAt = peewee.DateTimeField(default=datetime.utcnow())
    updatedAt = peewee.DateTimeField(default=datetime.utcnow())

