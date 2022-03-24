from peewee import *

db = SqliteDatabase('band_frame.db')

class BamdFrame(Model):
    time_table = ForeignKeyField(TimeTable, backref='band_frames')
    start_time = DateTimeField()
    end_time = DateTimeField()
    type = IntegerField()
    band = ForeignKeyField(Entry, backref='entry')

    class Meta:
        database = db # This model uses the "people.db" database.
