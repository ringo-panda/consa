from peewee import *

db = SqliteDatabase('time_table.db')

class TimeTable(Model):
    event = ForeignKeyField(Event, backref='time_tables')
    name = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.
