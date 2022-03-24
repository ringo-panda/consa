from peewee import *

db = SqliteDatabase('user_entry_relation.db')

class UserEntryRelation(Model):
    user = ForeignKeyField(User, backref='user_entry_relations')
    entry = ForeignKeyField(Entry, backref='user_entry_relations')

    class Meta:
        database = db # This model uses the "people.db" database.
