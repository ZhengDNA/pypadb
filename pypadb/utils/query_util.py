from typing import Any

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
