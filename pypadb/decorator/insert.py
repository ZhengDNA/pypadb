import functools
import re
from typing import Callable

from utils.query_util import execute


def insert(sql: str) -> Callable:
    arg_list = [s.strip() for s in re.findall(r'[(](.*?)[)]', sql)[0].split(',')]
    sql += ' values'

    def deco(fun):
        @functools.wraps(fun)
        def wrapper(data):
            in_sql = sql
            if not isinstance(data, list):
                template_sql = '('
                for arg in arg_list:
                    template_sql += f'%({arg})s,'
                template_sql = template_sql.rstrip(',') + '),'
                _, row_id = execute(in_sql + template_sql, data.dict())
                return row_id

            query_dict: dict = {}
            for i, v in enumerate(data):
                data_dict: dict = v.dict()
                query_dict = {**query_dict, **{f'{arg}{i}': data_dict.get(arg) for arg in arg_list}}
                in_sql += '('
                for item in arg_list:
                    in_sql += f'%({item}{i})s,'
                in_sql = in_sql.rstrip(',') + '),'

            _, row_id = execute(in_sql.rstrip(','), query_dict)
            return row_id

        return wrapper

    return deco
