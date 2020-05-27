#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：mark time:2020/5/26

from sqlalchemy.orm import state
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class SessionStatic(object):
    Session = None


def get_session_class():
    if SessionStatic.Session is not None:
        return SessionStatic.Session
    engine = create_engine(
        "mysql+mysqlconnector://root:@Dengppx123456@localhost:3306/scan?charset=utf8mb4",
        echo=True,
        max_overflow=0, pool_size=3, pool_timeout=30, pool_recycle=-1)
    Session = sessionmaker(bind=engine)
    SessionStatic.Session = Session;
    return Session


def get_session():
    session = scoped_session(get_session_class())
    session.configure(autocommit=True)
    return session


def transactional(method, *v):
    session = scoped_session(get_session_class())
    session.configure(autocommit=False)
    try:
        return method(session, *v)
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.commit()


def get_last_insert_id(session):
    sql = "select LAST_INSERT_ID()"
    r = session.execute(sql)
    return r.fetchone()[0]


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
    return session.execute(insert_sql, param)


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
    return session.execute(update_sql, param).rowcount


def query_page(session, page, count_sql, query_sql, cls, params):
    c_r = session.execute(count_sql, params)
    c = c_r.fetchone()[0]
    if c == 0:
        return []
    page.total_rows = c

    # // order by
    # 		if (!StringUtils.isEmpty(page.getOrderName())) {
    # 			qSql.append(" order by ").append(page.getOrderName()).append(" ").append(page.getOrderType());
    # 		}

    query_sql = query_sql + " limit :offset, :rows"
    params["offset"] = (int(page.page_number) - 1) * int(page.page_size);
    params["rows"] = int(page.page_size)
    r = session.query(cls).from_statement(text(query_sql)). \
        params(params).all()
    return r


