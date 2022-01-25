import abc
from typing import Any

from utils.enums import LikeEnum, QueryModeEnum


class Limit:
    __slots__ = ['start', 'count']

    start: int
    count: int

    def __init__(self, start: int, count: int = None):
        self.start = start
        self.count = count

    def __str__(self):
        if self.count is None:
            return f' limit {self.start}'
        return f' limit {self.start}, {self.count}'


class Like:
    __slots__ = ['sql', 'value', 'column']

    sql: str
    column: str
    value: str

    def __init__(self, column: str, value, like_type: LikeEnum):
        self.column = column
        self.value = value
        self.sql = f' {column} like'
        if like_type == LikeEnum.L_Like:
            self.sql += f' concat(\'%%\',%({column})s)'
        elif like_type == LikeEnum.R_Like:
            self.sql += f' concat(%({column})s,\'%%\')'
        elif like_type == LikeEnum.ALL_Like:
            self.sql += f' concat(\'%%\',%({column})s,\'%%\')'

    def __str__(self):
        return self.sql


class Extra(metaclass=abc.ABCMeta):
    __slots__ = ['column', 'data_property', 'method', 'mode']

    column: str
    data_property: str
    method: Any
    mode: QueryModeEnum


def extra(_column: list, _data_property: str, _method):
    """
    :param _column: table A[column[0]] mapping table B[column[1]]
    :param _data_property: table A property name
    :param _method: query method
    """

    class E(Extra):
        column = _column
        data_property = _data_property
        method = _method

        def __new__(cls, data_entity):
            if isinstance(data_entity, list):
                for entity in data_entity:
                    entity.__setattr__(cls.data_property,
                                       cls.method(**{cls.column[1]: data_entity.__getattribute__(cls.column[0])}))
                return data_entity
            data_entity.__setattr__(cls.data_property,
                                    cls.method(**{cls.column[1]: data_entity.__getattribute__(cls.column[0])}))
            return data_entity

    return E
