from flask import Flask
from flask_restful import Api, Resource
import importlib
import os

app = Flask(__name__)
api = Api(app)


controller = []
for dir_path, dir_names, filenames in os.walk(os.getcwd() + "/modules/"):
    for filename in filenames:
        if filename.endswith("_controller.py"):
            c_py = "modules" + dir_path.split("modules")[1].replace("/", ".") + "." + filename
            c_py = c_py.replace(".py", "")
            controller.append(c_py)

for c in controller:
    url_first = c.split(".")[-1].replace("_controller", "")
    modules = importlib.import_module(c)
    for i in dir(modules):
        if i.startswith("__") or i == "Resource":
            continue
        r = eval("modules." + i)
        if str(type(r)) == "<class 'flask.views.MethodViewType'>":
            api.add_resource(r, "/" + url_first + "/" + i)
            print("url:/" + url_first + "/" + i)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)