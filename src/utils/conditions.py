from utils.enums import LikeEnum


class Limit:
    __slots__ = ['start', 'count']

    start: str
    count: str

    def __init__(self, start: str, count: str = None):
        self.start = start
        self.count = count

    def __str__(self):
        if self.count is None:
            return f' limit %({self.start})s'
        return f' limit %({self.start})s, %({self.count})s'


class Like:
    __slots__ = ['sql']

    sql: str

    def __init__(self, variable: str, like_type: LikeEnum):
        self.sql = f' {variable} like'
        if like_type == LikeEnum.L_Like:
            self.sql += f' concat("%",%({variable}))'
        elif like_type == LikeEnum.R_Like:
            self.sql += f' concat(%({variable}),"%")'
        elif like_type == LikeEnum.ALL_Like:
            self.sql += f' concat("%",%({variable}),"%")'

    def __str__(self):
        return self.sql
