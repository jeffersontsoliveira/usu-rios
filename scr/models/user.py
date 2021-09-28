from SRC.database import BaseModel
from datetime import datetime
import peewee

class User(BaseModel):
    name = peewee.CharFiled()
    username = peewee.CharFiled()
    password = peewee.CharFiled()
    email = peewee.CharFiled(unique=True)
    admim = peewee.BooleanField(default=False)

    createdAt = peewee.DateTimeField(default = datetime.utcnow())
    updatedAt = peewee.DateTimeField(default = datetime.utcnow())

    class Meta:
        table_name = '_user'

