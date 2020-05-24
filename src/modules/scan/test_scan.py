
from flask_restful import Api, Resource


def test_url(u):
    print(u)


class HelloWorld(Resource):
    def get(self):
        return {'Hello': 'world001'}


class MyTest():
    def get(self):
        return "abc"

