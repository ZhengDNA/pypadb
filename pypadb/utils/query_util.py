from typing import Any

import connection_pool
from utils.enums import QueryModeEnum


def query(sql: str, kwargs: dict, data_type: Any, model: QueryModeEnum):
    conn: Any
    cur: Any
    try:
        conn = connection_pool.connection()
        cur = conn.cursor(connection_pool.cursor_type())
        cur.execute(sql, kwargs)

        first_data = cur.fetchone()
        if first_data is None:
            return None

        if model == QueryModeEnum.One:
            return data_type(**first_data)
        elif model == QueryModeEnum.Many:
            return [data_type(**first_data), *[data_type(**i) for i in cur.fetchall()]]
    finally:
        conn.close()
        cur.close()
