import flask_jwt
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse  # return data in JSON format
from flask_sqlalchemy import sqlalchemy
from sqlalchemy import exc

from models.item_model import ItemModel
from user_access_count import max_user_requests, max_requests_message


class Item(Resource):
    method_decorators = [jwt_required()]
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('price',
                             type=float,
                             required=True,
                             help="Price field must float and be present")
    post_parser.add_argument('in_store',
                             type=bool,
                             required=True,
                             help="Item needs in_store boolean key")

    @jwt_required()
    def get(self, item_name):
        if max_user_requests(flask_jwt.current_identity.username):
            return max_requests_message(), 400
        item = ItemModel.find_by_name(item_name)
        if item:
            return item.json(), 200
        else:
            return {"item": None}, 404

    @jwt_required()
    def post(self, item_name):
        if max_user_requests(flask_jwt.current_identity.username):
            return max_requests_message(), 400
        item = ItemModel.find_by_name(item_name)
        data = Item.post_parser.parse_args()
        if not item:
            item = ItemModel(item_name, data['price'], data['in_store'])  # **data
            try:
                item.save_to_database()
            except sqlalchemy.exc.DatabaseError:
                return {"message": "error - internal database error"}, 500
            else:
                return item.json(), 201  # created
        else:
            return {"message": "error - duplicated item name"}, 400  # bad request


class ItemsAmount(Resource):
    method_decorators = [jwt_required()]

    @jwt_required()
    def get(self):
        if max_user_requests(flask_jwt.current_identity.username):
            return max_requests_message(), 400

        return {'total items': ItemModel.count_all_items()}


class ItemsRange(Resource):
    method_decorators = [jwt_required()]

    @jwt_required()
    def get(self, start, stop):
        if max_user_requests(flask_jwt.current_identity.username):
            return max_requests_message(), 400
        max_stop = ItemModel.count_all_items()
        if (0 < stop <= max_stop) and (0 < start <= stop):
            return {'from': start, 'to': stop, 'items': [item.json() for item in ItemModel.get_range_items(start, stop)]}
        else:
            return {'error': 'invalid range', 'from': start, 'to': stop}