import functools
from typing import Callable

from utils import inspect_util
from utils.query_util import execute


def insert(sql: str) -> Callable:
    def deco(fun):
        @functools.wraps(fun)
        def wrapper(data):
            _, row_id = execute(sql, data.dict())
            return row_id

        return wrapper

    return deco
