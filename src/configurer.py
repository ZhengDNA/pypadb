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
        "closeable": False,
        "threadlocal": None,
        "host": "127.0.0.1",
        "user": "root",
        "password": "",
        "database": "test",
        "charset": "utf8",
    }

    def end(self) -> None:
        connection_pool.init_pool(self.__data)

    def set_creator(self, creator) -> 'Configurer':
        self.__data['creator'] = creator
        return self

    def set_maxconnections(self, maxconnections: int) -> 'Configurer':
        self.__data['maxconnections'] = maxconnections
        return self

    def set_(self) -> 'Configurer':
        self.__data[''] =
        return self

    def set_(self) -> 'Configurer':
        self.__data[''] =
        return self

    def set_(self) -> 'Configurer':
        self.__data[''] =
        return self

    def set_(self) -> 'Configurer':
        self.__data[''] =
        return self

    def set_maxusage(self, maxusage: int) -> 'Configurer':
        self.__data['creator'] = maxusage
        return self

    def set_setsession(self, setsession: list) -> 'Configurer':
        self.__data['setsession'] = setsession
        return self

    def set_(self) -> 'Configurer':
        self.__data[''] =
        return self

    def set_(self) -> 'Configurer':
        self.__data[''] =
        return self

    def set_(self) -> 'Configurer':
        self.__data[''] =
        return self

    def set_(self) -> 'Configurer':
        self.__data[''] =
        return self

    def set_(self) -> 'Configurer':
        self.__data[''] =
        return self

    def set_(self) -> 'Configurer':
        self.__data[''] =
        return self

    def set_(self) -> 'Configurer':
        self.__data[''] =
        return self
