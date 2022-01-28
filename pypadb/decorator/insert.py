import functools
import re
from typing import Callable

from utils.query_util import execute


def insert(sql: str) -> Callable:
    arg_list = [s.strip() for s in re.findall(r'[(](.*?)[)]', sql)[0].split(',')]
    sql += ' values'
    template_sql = '('
    for arg in arg_list:
        template_sql += f'%({arg})s,'
    template_sql = template_sql.rstrip(',') + ')'

    def deco(fun):
        @functools.wraps(fun)
        def wrapper(data):
            in_sql = sql
            if isinstance(data, list):
                for i in data:
                    in_sql += (template_sql % i.dict()) + ','
                _, row_id = execute(in_sql.rstrip(','))
                return row_id
            _, row_id = execute(in_sql + template_sql, data.dict())
            return row_id

        return wrapper

    return deco
