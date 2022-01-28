from typing import Any

from pydantic import BaseModel

import connection_pool
from utils.enums import QueryModeEnum


def query(sql: str, kwargs: dict, data_type: Any, model: QueryModeEnum):
    result_set, last_row_id = execute(sql, kwargs, connection_pool.cursor_type())
    if result_set is None:
        return None

    if model == QueryModeEnum.One:
        return data_type(**result_set[0]), last_row_id
    elif model == QueryModeEnum.Many:
        return [data_type(**i) for i in result_set], last_row_id


def execute(sql: str, kwargs: dict = None, cursor_type=None) -> tuple[list, int]:
    conn: Any
    cur: Any
    try:
        conn = connection_pool.connection()
        cur = conn.cursor(cursor_type) if cursor_type else conn.cursor()
        cur.execute(sql, kwargs)
        return cur.fetchall(), cur.lastrowid
    finally:
        conn.commit()
        conn.close()
        cur.close()


def parse_sql_batch(columns: list, data_list: list) -> tuple[str, dict]:
    query_dict: dict = {}
    query_sql: str = ''
    for i, v in enumerate(data_list):
        data_dict: dict = v.dict()
        query_dict = {**query_dict, **{f'{arg}{i}': data_dict.get(arg) for arg in columns}}
        query_sql += '('
        for item in columns:
            query_sql += f'%({item}{i})s,'
        query_sql = query_sql.rstrip(',') + '),'
    return query_sql.rstrip(','), query_dict
