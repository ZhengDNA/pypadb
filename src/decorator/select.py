import functools
from typing import Callable


def select(sql: str) -> Callable:
    def deco(fun: Callable):
        @functools.wraps(fun)
        def wrapper(*args, **kwargs):

            fun(*args, **kwargs)

        return wrapper

    return deco
