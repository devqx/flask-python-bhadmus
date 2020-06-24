from flask_restful import Resource, reqparse
from .models import UserModel

parser = reqparse.RequestParser()
parser.add_argument('username', help="the username field is a required", required=True)
parser.add_argument('password', help="the password is a required field", required=True)


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()

        new_user = UserModel(
            username=data['username'],
            password=data['password']
        )

        if UserModel.find_by_username(data['username']):
            return {
                       "success": False,
                       "error": [{
                           "username": "Username already exists"
                       }],
                       "message": "User {} already exists".format(data['username'])
                   }, 400

        try:
            new_user.save_user()
            return {
                "message": "User {} was created successfully".format(data['username'])
            }

        except:
            return {
                       "message": "User {} was not created successfully".format(data['username'])
                   }, 400


class AuthenticateUser(Resource):
    def post(self):
        request_body = parser.parse_args()

        username = request_body['username']

        current_user = UserModel.find_by_username(username)

        if not current_user:
            return {
                       "authenticated?": False,
                       "message": "User {} does not exist".format(request_body['username'])
                   }, 400

        if current_user.password == request_body['password']:
            return {
                "authenticated?": True,
                "message": "User {} logged in successful".format(request_body['username'])
            }

        else:
            return {
                "authenticated?": False,
                "message": "User {} does not exists".format(request_body['username'])
            }, 400
