from flask_pymongo import PyMongo
from bson.objectid import ObjectId

mongo = PyMongo()

class UserModel:
    def create_user(self, name, email, password):
        result = mongo.db.users.insert_one({
            'name': name,
            'email': email,
            'password': password
        })
        inserted_id = str(result.inserted_id)
        return inserted_id

    def get_users(self):
        users = []
        for doc in mongo.db.users.find():
            user = {
                '_id': str(doc['_id']),
                'name': doc['name'],
                'email': doc['email'],
                'password': doc['password']
            }
            users.append(user)
        return users

    def get_user(self, id):
        user = mongo.db.users.find_one({'_id': ObjectId(id)})
        if user:
            return {
                '_id': str(user['_id']),
                'name': user['name'],
                'email': user['email'],
                'password': user['password']
            }
        else:
            return None

    def delete_user(self, id):
        mongo.db.users.delete_one({'_id': ObjectId(id)})

    def update_user(self, id, name, email, password):
        mongo.db.users.update_one({'_id': ObjectId(id)}, {'$set': {
            'name': name,
            'email': email,
            'password': password
        }})