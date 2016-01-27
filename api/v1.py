# -*- coding: utf-8 -*-
'''
Copyright (c) 2013
@author: Marat Khayrullin <xmm.dev@gmail.com>
'''

from flask import Flask, Blueprint, request, jsonify
from flask_restful import reqparse, abort, Api, Resource

parser = reqparse.RequestParser()
# parser.add_argument('username', type=str, location='json')
# parser.add_argument('password', type=str, location='json')
# json_data = request.get_json(force=True)

API_VERSION_V1 = 1
API_VERSION = API_VERSION_V1

api_v1_bp = Blueprint('api_v1', __name__)
api_v1 = Api(api_v1_bp)


class AuthSignup(Resource):
    def post(self):
        # args = parser.parse_args()
        return {
            'hello': 'AuthSignup',
            'version': API_VERSION,
            }

class AuthSignin(Resource):
    def post(self):
        args = parser.parse_args()
        json_data = request.get_json(force=True)
        un = json_data['task']
        return jsonify(u=un)

class HelloWorld(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        un = json_data['task']
        return jsonify(u=un)

api_v1.add_resource(HelloWorld, '/testing')
api_v1.add_resource(AuthSignup, '/auth/signup')
api_v1.add_resource(AuthSignin, '/auth/signin')
