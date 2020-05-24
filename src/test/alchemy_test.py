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
    test_value = Column(String, nullable=True)


Session = sessionmaker(bind=engine)
session = Session()

r = session.query(Test).from_statement(
    text("SELECT test.*, 'abcefg' test_value FROM test where test_id=:id")).\
    params(id=1).all()

t = Test(test_id=None, test_name="abc")

print("------------")
print(t.__dict__)
for i in t.__dict__:
    print(type(getattr(t, i)) is not state.InstanceState)
print("============")
# session.commit()


# t = Test(test_id=None, test_name="abc")
# print(t)


print(r[0].test_value)