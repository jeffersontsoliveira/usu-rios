from peewee import PostegresqlDatabase, Model

connection = PostegresqlDatabase(
    'cadastro',
    user = 'root',
    password = 'root',
    host = 'localhost',
    port = '5432'
)

class BaseModel(Model):
    class Modal:
        database = connection