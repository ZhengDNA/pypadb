import inspect

from pypadb.table.base_table import BaseTable


class TableConfigurer:
    __slots__ = ['tables']

    tables: dict[str, BaseTable]

    def __init__(self):
        self.tables = {}

    def __getattr__(self, item: str) -> BaseTable:
        return self.tables[item]

    def __getitem__(self, item: str) -> BaseTable:
        return self.tables[item]

    def init_tables(self, module_=None, escape_upper: bool = False, **kwargs):
        if inspect.ismodule(module_):
            module_dict: dict = {}
            for i in inspect.getmembers(__import__('entities')):
                member_name = i[0][0].lower()
                for ch in i[0][1:]:
                    if ch.isupper() and not escape_upper:
                        member_name += '_'
                    member_name += ch.lower()
                module_dict[member_name] = i[1]
            self.tables = {**self.tables, **{key: BaseTable(key, module_dict[key]) for key in module_dict}}
        if kwargs:
            self.tables = {**self.tables, **{key: BaseTable(key, kwargs[key]) for key in kwargs}}


tables: TableConfigurer = TableConfigurer()
