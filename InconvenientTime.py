from peewee import *

db = SqliteDatabase('inconvenient_time.db')

class InconvenientTime(Model):
    user = ForeignKeyField(User, backref='inconvenient_times')
    start_time = DateTimeField()
    end_time = DateTimeField()

    class Meta:
        database = db # This model uses the "people.db" database.
