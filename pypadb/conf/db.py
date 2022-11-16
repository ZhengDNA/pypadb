from typing import List

import pymysql

from pypadb.connection_pool import _init_pool


class DbConfig:
    __data: dict = {
        "creator": pymysql,
        "maxconnections": 6,
        "mincached": 2,
        "maxcached": 5,
        "blocking": True,
        "maxusage": None,
        "setsession": [],
        "ping": 0,
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "123456",
        "database": "test",
        "charset": "utf8",
        "cursor": pymysql.cursors.DictCursor
    }

    def end(self) -> None:
        _init_pool(**self.__data)

    def set_creator(self, creator) -> 'DbConfig':
        self.__data['creator'] = creator
        return self

    def set_maxconnections(self, maxconnections: int) -> 'DbConfig':
        self.__data['maxconnections'] = maxconnections
        return self

    def set_mincached(self, mincached: int) -> 'DbConfig':
        self.__data['mincached'] = mincached
        return self

    def set_maxcached(self, maxcached: int) -> 'DbConfig':
        self.__data['maxcached'] = maxcached
        return self

    def set_blocking(self, blocking: bool) -> 'DbConfig':
        self.__data['blocking'] = blocking
        return self

    def set_maxusage(self, maxusage: int) -> 'DbConfig':
        self.__data['creator'] = maxusage
        return self

    def set_setsession(self, setsession: List[str]) -> 'DbConfig':
        self.__data['setsession'] = setsession
        return self

    def set_host(self, host: str) -> 'DbConfig':
        self.__data['host'] = host
        return self

    def set_port(self, port: int) -> 'DbConfig':
        self.__data['port'] = port
        return self

    def set_user(self, user: str) -> 'DbConfig':
        self.__data['user'] = user
        return self

    def set_password(self, password: str) -> 'DbConfig':
        self.__data['password'] = password
        return self

    def set_database(self, database: str) -> 'DbConfig':
        self.__data['database'] = database
        return self

    def set_charset(self, charset: str) -> 'DbConfig':
        self.__data['charset'] = charset
        return self

    def set_cursor(self, cursor) -> 'DbConfig':
        self.__data['cursor'] = cursor
        return self


db_config: DbConfig = DbConfig()
