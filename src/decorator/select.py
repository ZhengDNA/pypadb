import functools
from types import GenericAlias
from typing import Callable, Any

import pymysql.cursors

import connection_pool
from exception import RequireReturnTypeAnnotation
from utils import inspect_utils


def select(sql: str, data_type: Any) -> Callable:
    def deco(fun: Callable):
        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            conn = connection_pool.connection()
            cur = conn.cursor(connection_pool.cursor_type())

            cur.execute(sql, dict(zip([a.name for a in inspect_utils.arg_list(fun)], args)))
            func_returns = inspect_utils.returns_type(fun)

            if not func_returns:
                raise RequireReturnTypeAnnotation('require return type annotation')

            if func_returns == GenericAlias(list, data_type):
                return [data_type(**i) for i in cur.fetchall()]
            else:
                return data_type(**cur.fetchone())

        return wrapper

    return deco
