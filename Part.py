from peewee import *

db = SqliteDatabase('part.db')

class Part(Model):
    user = ForeignKeyField(User, backref='parts')
    name = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.


