from peewee import *

db = SqliteDatabase('position.db')

class Positon(Model):
    user = ForeignKeyField(User, backref='positions')
    name = CharField()
    year = IntegerField()

    class Meta:
        database = db # This model uses the "people.db" database.
