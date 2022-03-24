from peewee import *

db = SqliteDatabase('membership_fee.db')

class MemberShipFee(Model):
    user = ForeignKeyField(User, backref='membership_fees')
    name = CharField()
    price = IntegerField()
    status = BooleanField()
    payment_method = IntegerField()
    receipt_date = DateField()
    receipt_user = ForeignKeyField(User)

    class Meta:
        database = db # This model uses the "people.db" database.
