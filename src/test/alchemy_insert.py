# !/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import test
import sys
sys.path.append('../common')
import db_utils


engine = create_engine(
    "mysql+mysqlconnector://root:@Dengppx123456@localhost:3306/scan?charset=utf8mb4",
    echo=True,
    max_overflow=5)

Session = sessionmaker(bind=engine)
session = Session()

test = test.Test(test_id=29, test_name="xde99999")
test.test_date = '2020-10-11'
test.test_value = 13.99
test.test_type = 3
db_utils.update(session, test)
session.commit()





