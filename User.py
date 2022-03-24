from peewee import *

db = SqliteDatabase('user.db')

class User(Model):
    email = CharField()
    password = CharField()
    name = CharField()
    kana = CharField()
    grade = IntegerField()
    graduate_year = IntegerField()

    class Meta:
        database = db # This model uses the "people.db" database.
