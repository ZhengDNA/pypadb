import inspect
from typing import Any, Optional

from pydantic import BaseModel

from exception import ArgNotCallable


class Argument(BaseModel):
    __slots__ = ('name', 'type', 'default')
    name: str
    type: Optional[type]
    default: Any


def arg_list(fun) -> list[Argument]:
    if not callable(fun):
        raise ArgNotCallable(fun)
    return [Argument(name=tp[0],
                     type=tp[1].annotation if tp[1].annotation != inspect._empty else None,
                     default=tp[1].default if tp[1].default != inspect._empty else None)
            for tp in inspect.signature(fun).parameters.items()]


def returns_val(fun) -> type:
    a = inspect.signature(fun).return_annotation
    return a if a != inspect._empty else None
