
from sqlalchemy.orm import class_mapper
from flask import request, jsonify
import src.common.req_utils as req_utils
import src.common.json_utils as json_utils
import src.common.db_utils as db_utils
from src.common.page import Page
from src.test.test import Test
from sqlalchemy import Column, Integer, String, text, Date, DateTime, DECIMAL


# id_list=[1, 2, 3]
# sql = text("UPDATE test SET name='hello' WHERE id in :id_list")
# db.session.execute(sql, id_list=tuple(id_list))


def go(page):
    page.total_rows = 100

    count_sql = "select count(*) from test where test_id=:id"
    query_sql = "select * from test where test_id=:id"
    session = db_utils.get_session();

    params = {'id': 29}
    r = db_utils.query_page(session, page, count_sql, query_sql, Test, params)
    return json_utils.to_json(r)
