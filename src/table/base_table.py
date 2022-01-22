from typing import Any

from utils.conditions import Limit, Like
from utils.query_util import query


class BaseTable:
    __slots__ = ['name', 'data_type']
    name: str
    data_type: Any

    def __init__(self, name: str, data_type):
        self.name = name
        self.data_type = data_type

    def select_one(self, **kwargs):
        return query(self.__parse_sql(kwargs), kwargs, self.data_type, 'one')

    def select_many(self, conditions: dict = {}, limit: Limit = None) -> list:
        return query(self.__parse_sql(conditions, limit), conditions, self.data_type, 'many')

    def __parse_sql(self, conditions: dict, limit: Limit) -> str:
        sql: str = f'select * from {self.name}'
        if conditions:
            sql += ' where'
            for key in conditions:
                sql += f' {key}=%({key})s and'
        sql = sql.rstrip(' and')
        return sql + str(limit) if limit else sql
