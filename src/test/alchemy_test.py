# !/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, state

from src.test.test import Test
import json

from datetime import datetime

from sqlalchemy.ext.declarative import DeclarativeMeta


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    if isinstance(data, datetime):
                        data=data.strftime('%Y-%m-%d %H:%M:%S')
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None


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
print(len(r))
print(type(r))

Hosts = []
for rr in r:
    Hosts.append(json.dumps(rr, cls=AlchemyEncoder))
print(json.dumps(Hosts))