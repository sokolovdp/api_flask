from werkzeug.security import check_password_hash

import user_access_count
from models.user_model import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and check_password_hash(user.password_hash, password):
        user_access_count.reset_user_counter(user.username)
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
