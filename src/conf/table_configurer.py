from table import BaseTable


class TableConfigurer:
    __slots__ = ['tables']

    tables: list[BaseTable]

    def __init__(self, **kwargs):
        self.tables = []
        for key in kwargs:
            self.tables.append(BaseTable(key, kwargs.get(key)))

    def __getattr__(self, item: str) -> BaseTable:
        return self[item]

    def __getitem__(self, item) -> BaseTable:
        if isinstance(item, int):
            return self.tables[item]
        if isinstance(item, str):
            for table in self.tables:
                if table.name == item:
                    return table
        return None
