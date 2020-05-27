
from flask_restful import Api, Resource
from flask import request, jsonify
from src.common.page import Page
import src.common.req_utils as req_utils
from src.test.test import Test
import src.modules.scan.test_impl as impl
import src.common.json_utils as json_utils


class HelloWorld(Resource):
    def get(self):
        page = req_utils.req_to_object(request, Page)
        print("---------")
        print(jsonify(page))
        print(request.args.get("username"))

        test = req_utils.req_to_object(request, Test)
        print("===========")
        print(test.test_value)
        return {'Hello': 'world001'}


class MyTest(Resource):
    def get(self):
        page = req_utils.req_to_object(request, Page)
        page_list = impl.go(page)
        return jsonify({"error_code:": 0, "page": json_utils.as_dict(page), "page_list": page_list})

