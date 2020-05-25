# !/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, text, Date, DateTime, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, state

from decimal import *
from datetime import *

from src.test.test import Test

import json

from datetime import datetime

from sqlalchemy.ext.declarative import DeclarativeMeta


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj.__class__, DeclarativeMeta):
            return None
        fields = {}
        for field in obj.__dict__:
            field_val = getattr(obj, field)
            if field_val is None or type(field_val) is state.InstanceState:
                continue
            if type(field_val) is datetime:
                field_val = field_val.strftime('%Y-%m-%d %H:%M:%S')
            elif type(field_val) is date:
                field_val = field_val.strftime('%Y-%m-%d')
            elif type(field_val) is Decimal:
                print(field_val)
                field_val = '%.2f' % field_val
            fields[field] = field_val
        return fields


engine = create_engine(
    "mysql+mysqlconnector://root:@Dengppx123456@localhost:3306/scan?charset=utf8mb4",
    echo=True,
    max_overflow=5)

Base = declarative_base()


Session = sessionmaker(bind=engine)
session = Session()

#  Test.test_value.label("test_value") session.commit()用
r = session.query(Test).from_statement(
    text("SELECT test.* FROM test where test_id=:id")).\
    params(id=29).all()
# t = Test(test_id=None, test_name="abc")
# print(t)
# print(len(r))
print("---------begin")
print(r)
print("---------end")

print(json.dumps(r, cls=AlchemyEncoder))