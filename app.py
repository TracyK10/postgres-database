import os

from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class UserView(Resource):
    def get(self):
        return '<h1>Welcome to my user app</h1>'
    
api.add_resource(UserView, '/')

class UserResource(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return make_response(jsonify(users), 200)
        
api.add_resource(UserResource, '/users')

if __name__ == '__main__':
    app.run(debug=True)
