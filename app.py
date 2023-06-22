from flask import Flask
from flask_cors import CORS
from model import mongo
from controller import UserController

app = Flask(__name__)
CORS(app)
app.config['MONGO_URI'] = 'mongodb://localhost/pythonreactdb'
mongo.init_app(app)

controller = UserController()

@app.route('/users', methods=['POST'])
def create_user():
    return controller.create_user()

@app.route('/users', methods=['GET'])
def get_users():
    return controller.get_users()

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    return controller.get_user(id)

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    return controller.delete_user(id)

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    return controller.update_user(id)

if __name__ == "__main__":
    app.run(debug=True)
