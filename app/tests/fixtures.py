import json
from app.configs import cnf
from app.utils.db import dal
from pathlib import Path
import os
from datetime import datetime as dt, timedelta

BASE_DIR = Path(__file__).resolve().parent.parent
SAMPLE_DATA_PATH = os.path.join(BASE_DIR, "tests/sampledata")


def object_hook(obj):
    outDict = {}
    for k, v in obj.items():
        if k in ["startdate", "dateofbirth"]:
            outDict[k] = dt.strptime(v, "%Y-%m-%d").date()
        elif k == "enddate":
            if v == "2022-12-14":
                outDict[k] = (dt.now() + timedelta(days=1)).date()
            else:
                outDict[k] = dt.strptime(v, "%Y-%m-%d").date()
        else:
            outDict[k] = v
    return outDict


def get_json_from_file(table_name):
    with open(os.path.join(SAMPLE_DATA_PATH, f"{table_name}.json"), "r") as f:
        data_json = json.load(f, object_hook=object_hook)
    return data_json


def __insert_data(tabledesc):
    schema, table_name = tabledesc.split(":")
    ins = dal.get_table(table_name=table_name, schema=schema).insert()
    data_json = get_json_from_file(table_name)
    dal.connection.execute(ins, data_json)


def populate_db_with_sample_data():
    __insert_data(cnf.APP_CONFIG.CTCN_COMUNI_)
    __insert_data(cnf.APP_CONFIG.CTCN_SEZIONI_)
    __insert_data(cnf.APP_CONFIG.CTMP_FOGLI)
    __insert_data(cnf.APP_CONFIG.CTMP_FABRICATI)
    __insert_data(cnf.APP_CONFIG.CTMP_PARTICELLE)
    __insert_data(cnf.APP_CONFIG.CTCN_COMUNI)
    __insert_data(cnf.APP_CONFIG.CTCN_CTQUALIT)
    __insert_data(cnf.APP_CONFIG.CTCN_CTPARTIC)
    __insert_data(cnf.APP_CONFIG.CTCN_CUARCUIU)
    __insert_data(cnf.APP_CONFIG.CTCN_CUIDENTI)
    __insert_data(cnf.APP_CONFIG.CTCN_CTFISICA)
    __insert_data(cnf.APP_CONFIG.CTCN_CTNONFIS)
    __insert_data(cnf.APP_CONFIG.CTCN_CTTITOLA)
    __insert_data(cnf.APP_CONFIG.CTCN_CTTITOLI)
    __insert_data(cnf.APP_CONFIG.CTCN_CUCODTOP)
    __insert_data(cnf.APP_CONFIG.CTCN_CUINDIRI)
