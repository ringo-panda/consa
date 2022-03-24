from asyncio import events
from peewee import *

db = SqliteDatabase('payment.db')

class Payment(Model):
    user = ForeignKeyField(User, backref='payments')
    event = ForeignKeyField(Event, backref='payment')
    price = IntegerField()
    status = BooleanField()
    payment_method = IntegerField()
    receipt_date = DateField()
    receipt_user = ForeginKeyField(User)

    class Meta:
        database = db # This model uses the "people.db" database.
