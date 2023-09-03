from flask_login import UserMixin


class User(UserMixin):
    pass


users = [
    {'id': 'admin', 'username': 'admin', 'password': 'admin'},
    {'id': '123', 'username': '123', 'password': '123'}
]


def query_user(user_id):
    for user in users:
        if user_id == user['id']:
            return user
