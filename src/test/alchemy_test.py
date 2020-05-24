# !/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, state

engine = create_engine(
    "mysql+mysqlconnector://root:@Dengppx123456@localhost:3306/scan?charset=utf8mb4",
    echo=True,
    max_overflow=5)

Base = declarative_base()



class Test(Base):
    __tablename__ = 'test'
    test_id = Column(Integer, primary_key=True)
    test_name = Column(String)
    test_value = Column(String)
    test_value2 = Column(String)

Session = sessionmaker(bind=engine)
session = Session()


r = session.query(Test, Test.test_value.label("test_value"),
        Test.test_value2.label("test_value2")) .from_statement(
    text("SELECT test.*, 'abcefg' test_value, 'abcef2g' test_value2 FROM test where test_id=:id")).\
    params(id=1).all()


session.execute("insert into test(test_name) values(:test_name)", {"test_name":"sxs's"})

session.commit()


#
# t = Test(test_id=None, test_name="abc")
# print("------------")
# print(t.__dict__)
# for i in t.__dict__:
#     if type(getattr(t, i)) is state.InstanceState:
#         continue
#     print(getattr(Test, i).primary_key)
# print("============")



# t = Test(test_id=None, test_name="abc")
# print(t)


print(r[0].test_value)