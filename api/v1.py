from flask import Flask, Blueprint, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from api.auth import Signup, Signin

parser = reqparse.RequestParser()
# parser.add_argument('username', type=str, location='json')
# json_data = request.get_json(force=True)

API_VERSION_V1 = 1
API_VERSION = API_VERSION_V1

api_v1_bp = Blueprint('api_v1', __name__)
api_v1 = Api(api_v1_bp)


class AuthSignup(Resource):
    def post(self):
        # args = parser.parse_args()
        json_data = request.get_json(force=True)
        method = json_data['type']
        auc = Signup()
        methodCall = getattr(auc, method, 0)
        if not methodCall:
            return {'error': 'Not method auth'}, 400
        else:
            return methodCall(json_data['user'], json_data['pswd'])

class AuthSignin(Resource):
    def post(self):
        # args = parser.parse_args()
        json_data = request.get_json(force=True)
        method = json_data['type']
        auc = Signin()
        methodCall = getattr(auc, method, 0)
        if not methodCall:
            return {'error': 'Not method auth'}, 400
        else:
            return methodCall(json_data['user'], json_data['pswd'])


api_v1.add_resource(AuthSignup, '/auth/signup')
api_v1.add_resource(AuthSignin, '/auth/signin')
