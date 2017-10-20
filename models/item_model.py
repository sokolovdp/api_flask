# from flask_sqlalchemy import sqlalchemy
from sqlalchemy import func

from db_alchemy import db


class ItemModel(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    product_image = db.Column(db.String(255), unique=True, nullable=True)
    in_store = db.Column(db.Boolean(), unique=False, nullable=False)

    def __init__(self, item_name, item_price, item_in_store):
        self.name = item_name
        self.price = item_price
        self.in_store = item_in_store

    def json(self):
        return {'name': self.name, 'price': self.price, 'in_store': self.in_store}

    @classmethod
    def find_by_name(cls, item_name):
        return cls.query.filter_by(name=item_name).first()

    def save_to_database(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_database(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_range_items(cls, start, stop):
        # result = cls.query.all()[start:stop]
        result = db.session.query(ItemModel).filter(ItemModel.id.between(start, stop))
        return result

    @classmethod
    def count_all_items(cls):
        # count = len(cls.query.all())
        number_of_records = db.session.query(func.count(ItemModel.id)).scalar()
        return number_of_records
