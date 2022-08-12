import functools
from typing import Callable, Any, List

from pypadb.connection_pool import cursor_type, connection
from pypadb.exception import RequireReturnTypeAnnotation
from pypadb.utils import inspect_util


def select(sql: str, data_type: Any) -> Callable:
    def deco(fun: Callable):
        @functools.wraps(fun)
        def wrapper(*args):
            conn = connection()
            with conn:
                cur = conn.cursor(cursor_type())
                cur.execute(sql, dict(zip([a.name for a in inspect_util.arg_list(fun)], args)))
                func_returns = inspect_util.returns_type(fun)

                if not func_returns:
                    raise RequireReturnTypeAnnotation('require return type annotation')

                first_data = cur.fetchone()
                if first_data is None:
                    return None

                if func_returns == List[data_type]:
                    return [data_type(**first_data), *[data_type(**i) for i in cur.fetchall()]]
                else:
                    return data_type(**first_data)

        return wrapper

    return deco
