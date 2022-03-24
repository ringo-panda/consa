from peewee import *

db = SqliteDatabase('entry.db')

class Entry(Model):
    event = ForeignKeyField(Event, backref='entries')
    band_master = ForeignKeyField(User)
    band_name = CharField()
    appeal = CharField()
    remarks = CharField()


    class Meta:
        database = db # This model uses the "people.db" database.
