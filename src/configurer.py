import pymysql

import connection_pool


class Configurer():
    __data: dict = {
        "creator": pymysql,
        "maxconnections": 6,
        "mincached": 2,
        "maxcached": 5,
        "maxshared": 3,
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
        connection_pool._init_pool(**self.__data)

    def set_creator(self, creator) -> 'Configurer':
        self.__data['creator'] = creator
        return self

    def set_maxconnections(self, maxconnections: int) -> 'Configurer':
        self.__data['maxconnections'] = maxconnections
        return self

    def set_mincached(self, mincached: int) -> 'Configurer':
        self.__data['mincached'] = mincached
        return self

    def set_maxcached(self, maxcached: int) -> 'Configurer':
        self.__data['maxcached'] = maxcached
        return self

    def set_maxshared(self, maxshared: int) -> 'Configurer':
        self.__data['maxshared'] = maxshared
        return self

    def set_blocking(self, blocking: bool) -> 'Configurer':
        self.__data['blocking'] = blocking
        return self

    def set_maxusage(self, maxusage: int) -> 'Configurer':
        self.__data['creator'] = maxusage
        return self

    def set_setsession(self, setsession: list[str]) -> 'Configurer':
        self.__data['setsession'] = setsession
        return self

    def set_host(self, host: str) -> 'Configurer':
        self.__data['host'] = host
        return self

    def set_port(self, port: int) -> 'Configurer':
        self.__data['port'] = port
        return self

    def set_user(self, user: str) -> 'Configurer':
        self.__data['user'] = user
        return self

    def set_password(self, password: str) -> 'Configurer':
        self.__data['password'] = password
        return self

    def set_database(self, database: str) -> 'Configurer':
        self.__data['database'] = database
        return self

    def set_charset(self, charset: str) -> 'Configurer':
        self.__data['charset'] = charset
        return self

    def set_cursor(self, cursor) -> 'Configurer':
        self.__data['cursor'] = cursor
        return self
