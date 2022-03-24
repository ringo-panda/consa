from peewee import *

db = SqliteDatabase('music.db')

class Music(Model):
    entry = ForeignKeyField(Entry, backref='musics')
    song_title = CharField()
    acoustic_request = CharField()
    staging_request = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.
