from typing import Any, Union

from utils.conditions import Limit, Like
from utils.enums import QueryModeEnum
from utils.query_util import query


class BaseTable:
    __slots__ = ['name', 'data_type', 'base_select_sql']

    name: str
    data_type: Any
    base_select_sql: str

    def __init__(self, name: str, data_type):
        self.name = name
        self.data_type = data_type
        self.base_select_sql = f'select * from {name}'

    def select_one(self, extra=None, **kwargs):
        res = query(self.__parse_sql(kwargs), kwargs, self.data_type, QueryModeEnum.One)
        return extra(res) if extra else res

    def select_many(self, limit: Limit = None, extra=None, **kwargs) -> list:
        res = query(self.__parse_sql(kwargs, limit), kwargs, self.data_type, QueryModeEnum.Many)
        return extra(res) if extra else res

    def select_like(self,
                    likes: Union[list[Like], Like] = {},
                    limit: Limit = None,
                    extra=None) -> list:
        sql: str = self.base_select_sql
        data_dict: dict = {}
        if likes:
            sql += ' where'
            if isinstance(likes, list):
                for like in likes:
                    sql += f'{like} and'
                    data_dict[like.column] = like.value
                sql = sql.rstrip(' and')
            else:
                sql += str(likes)
                data_dict[likes.column] = likes.value
        res = query(sql + str(limit) if limit else sql, data_dict, self.data_type, QueryModeEnum.Many)
        return extra(res) if extra else res

    def __parse_sql(self, conditions: dict, limit: Limit = None) -> str:
        sql: str = self.base_select_sql
        if conditions:
            sql += ' where'
            for key in conditions:
                sql += f' {key}=%({key})s and'
        sql = sql.rstrip(' and')
        return sql + str(limit) if limit else sql

    def update_by_primary(self):
        pass

    def delete_by_primary(self):
        pass

    def insert(self, data):
        pass

    def insert_batch(self, data: list):
        pass
