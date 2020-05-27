#!/usr/bin/python
# -*- coding: utf-8 -*-
# author：mark time:2020/5/27
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, text, Date, DateTime, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, state
import json
from sqlalchemy.ext.declarative import DeclarativeMeta
from decimal import *
from datetime import *
from flask import request, jsonify


def as_dict(obj):
    fields = {}
    for field in obj.__dict__:
        field_val = getattr(obj, field)
        if field.startswith("__"):
            continue
        if field_val is None or type(field_val) is state.InstanceState:
            continue
        if type(field_val) is datetime:
            field_val = field_val.strftime('%Y-%m-%d %H:%M:%S')
        elif type(field_val) is date:
            field_val = field_val.strftime('%Y-%m-%d')
        elif type(field_val) is Decimal:
            field_val = '%.2f' % field_val
        fields[field] = field_val
    return fields


def to_json_obj(obj):
    fields = {}
    for field in obj.__dict__:
        field_val = getattr(obj, field)
        print(field_val)
        if field_val is None or type(field_val) is state.InstanceState:
            continue
        if type(field_val) is datetime:
            field_val = field_val.strftime('%Y-%m-%d %H:%M:%S')
        elif type(field_val) is date:
            field_val = field_val.strftime('%Y-%m-%d')
        elif type(field_val) is Decimal:
            field_val = '%.2f' % field_val
        fields[field] = field_val
    return fields


def to_json(list):
    return_list = []
    for obj in list:
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
                field_val = '%.2f' % field_val
            fields[field] = field_val
        return_list.append(fields)
    return return_list



