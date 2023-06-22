from flask import request
from bson.objectid import ObjectId
from model import UserModel
from view import UserView


user_model = UserModel()
user_view = UserView()

class UserController:
    def create_user(self):
        data = request.json
        inserted_id = user_model.create_user(data['name'], data['email'], data['password'])
        return user_view.render_user(inserted_id)

    def get_users(self):
        users = user_model.get_users()
        return user_view.render_users(users)

    def get_user(self, id):
        user = user_model.get_user(id)
        return user_view.render_user(user)

    def delete_user(self, id):
        user_model.delete_user(id)
        return user_view.render_deleted()

    def update_user(self, id):
        data = request.json
        user_model.update_user(id, data['name'], data['email'], data['password'])
        return user_view.render_updated()
