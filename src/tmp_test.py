import importlib

import sys
import os


# controller = []
# for dir_path, dir_names, filenames in os.walk(os.getcwd() + "/modules/"):
#     for filename in filenames:
#         if filename.endswith("_controller.py"):
#             c_py = "modules" + dir_path.split("modules")[1].replace("/", ".") + "." + filename
#             c_py = c_py.replace(".py", "")
#             controller.append(c_py)
# print(controller)
#
# for c in controller:
#     url = []
#     modules = importlib.import_module(c)
#     for i in dir(modules):
#         if i.startswith("__") or i == "Resource":
#             continue
#         r = eval("modules." + i)
#         if str(type(r)) == "<class 'flask.views.MethodViewType'>":
#             url.append(i)
#     print(url)


