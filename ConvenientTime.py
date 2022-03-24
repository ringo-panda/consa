from peewee import *

db = SqliteDatabase('convenient_time.db')

class ConvenientTime(Model):
    user = ForeignKeyField(User, backref='convenient_times')
    start_time = DateTimeField()
    end_time = DateTimeField()

    class Meta:
        database = db # This model uses the "people.db" database.
