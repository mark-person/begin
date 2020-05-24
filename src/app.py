from flask import Flask
from flask_restful import Api, Resource

import importlib


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'Hello': 'world'}


aa = importlib.import_module('modules.scan.test_scan')



api.add_resource(HelloWorld, "/")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)