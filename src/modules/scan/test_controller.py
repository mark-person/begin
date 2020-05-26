
from flask_restful import Api, Resource
from flask import request
from src.common.page import Page
import src.common.req_utils as req_utils
from src.test.test import Test

class HelloWorld(Resource):
    def get(self):
        page = req_utils.req_to_object(request, Page)
        print("---------")
        print(page.page_number)
        print(request.args.get("username"))

        test = req_utils.req_to_object(request, Test)
        print("===========")
        print(test.test_value)
        return {'Hello': 'world001'}


class MyTest(Resource):
    def get(self):
        return "abc"

