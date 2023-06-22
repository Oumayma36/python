from flask import jsonify

class UserView:
    def render_users(self, users):
        return jsonify(users)

    def render_user(self, user):
        if user:
            return jsonify(user)
        else:
            return jsonify({'message': 'User not found'})

    def render_deleted(self):
        return jsonify({'msg': 'User deleted'})

    def render_updated(self):
        return jsonify({'msg': 'User Updated'})
