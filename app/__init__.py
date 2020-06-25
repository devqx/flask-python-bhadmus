from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
app = Flask(__name__, instance_relative_config=True)
api = Api(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLACHEMY_TRACK_MDOFICATIONS'] = False
app.config['SECRET_KEY'] = "badmus_software_engineer_in_practice"
app.config['JWT_SECRET_KEY'] = "badmus_software_engineer_in_practice"

app.config.from_object('config')
db = SQLAlchemy(app)
jwt = JWTManager(app)

from . import views, resources
api.add_resource(resources.UserRegistration, '/users')
api.add_resource(resources.AuthenticateUser, '/auth/login')
api.add_resource(resources.GetUsers, '/users')
api.add_resource(resources.GetIdentity, '/auth/user')

@app.before_first_request
def create_tables():
    db.create_all()
