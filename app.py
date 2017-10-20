import os

from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.item import Item, ItemsRange, ItemsAmount
from resources.user import UserRegister
from security import authenticate, identity

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///api_data.db')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL',
#                                                       'postgresql://postgres:politruk@localhost:5432/api_data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sokolov'

api = Api(app)
jwt = JWT(app, authentication_handler=authenticate, identity_handler=identity)  # /auth - route handler
api.add_resource(Item, '/items/<string:item_name>')
api.add_resource(ItemsAmount, '/items')
api.add_resource(ItemsRange, '/items/<int:start>/<int:stop>')
api.add_resource(UserRegister, '/signup')

if __name__ == '__main__':
    from db_alchemy import db

    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=8000)
