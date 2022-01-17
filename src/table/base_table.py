from typing import Any

from utils import query


class BaseTable:
    __slots__ = ['name', 'data_type']
    name: str
    data_type: Any

    def __init__(self, name: str, data_type):
        self.name = name
        self.data_type = data_type

    def select_one(self, **kwargs):
        return query(self.__parse_sql(kwargs), kwargs, self.data_type, 'one')

    def select_many(self, **kwargs) -> list:
        return query(self.__parse_sql(kwargs), kwargs, self.data_type, 'many')

    def __parse_sql(self, kwargs: dict) -> str:
        sql: str = f'select * from {self.name} '
        if kwargs:
            sql += 'where '
            for key in kwargs:
                sql += f'{key}=%({key})s and '
        return sql.rstrip('and ')
