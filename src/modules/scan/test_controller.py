
from flask_restful import Api, Resource
from flask import request


class HelloWorld(Resource):
    def get(self):
        print(request.args.get("username"))
        return {'Hello': 'world001'}


class MyTest(Resource):
    def get(self):
        return "abc"

