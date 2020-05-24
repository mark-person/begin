import importlib

import sys

aa = importlib.import_module('modules.scan.test_scan')

print(dir(aa))

r = eval("aa.MyTest")()
print(r)

