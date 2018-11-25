from flask import jsonify, Blueprint, abort
from flask_restful import (Resource, Api, reqparse, inputs, fields,
                           marshal, marshal_with)

import models

user_fields = {
    'username': fields.String,
    'email': fields.String,
    'password': fields.String
}


# TODO create UserList() with a post that will create a new user
class UserList(Resource):
    def __init__(self):
        """
        Input validation using reqparse
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            required=True,
            help='No username provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'email',
            required=True,
            help='No email provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'password',
            required=True,
            help='No password provided',
            location=['form', 'json']
        )
