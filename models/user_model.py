from db_alchemy import db


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password_hash = db.Column(db.String(180))

    def __init__(self, user_name, password_hash):
        self.username = user_name
        self.password_hash = password_hash

    @classmethod
    def find_by_username(cls, user_name):
        return cls.query.filter_by(username=user_name).first()

    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()

    def save_to_database(self):
        db.session.add(self)
        db.session.commit()
