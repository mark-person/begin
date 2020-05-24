# !/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy.orm import state


def insert(session, entity):
    col_name = []
    col_value = []
    for field in entity.__dict__:
        field_val = getattr(entity, field)
        if field_val is None or type(field_val) is state.InstanceState:
            continue
        col_name.append(field)
        col_value.append(field_val)
    insert_sql = "insert into " + entity.__tablename__ + "(" + ",".join(col_name) \
                 + ") values(:" + ",:".join(col_name) + ")"
    param = {}
    for index, k in enumerate(col_name):
        param[k] = col_value[index]
    session.execute(insert_sql, param)


def update(session, entity):
    col_name = []
    col_set = []
    col_value = []
    primary_name = ""
    primary_value = None
    for field in entity.__dict__:
        field_val = getattr(entity, field)
        if field_val is None or type(field_val) is state.InstanceState:
            continue
        if getattr(entity.__class__, field).primary_key:
            primary_name = field
            primary_value = field_val
            continue
        col_name.append(field)
        col_set.append(field + "= :" + field)
        col_value.append(field_val)
    update_sql = "update " + entity.__tablename__ + " set " + ",".join(col_set) \
                 + " where " + primary_name + " = :" + primary_name
    param = {}
    for index, k in enumerate(col_name):
        param[k] = col_value[index]
    param[primary_name] = primary_value
    session.execute(update_sql, param)


