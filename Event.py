from peewee import *

db = SqliteDatabase('event.db')

class Event(Model):
    start_date = DateField()
    end_date = DateField()
    venue = CharField()
    comment = TextField()
    status = IntegerField()
    expense = IntegerField()

    class Meta:
        database = db # This model uses the "people.db" database.
