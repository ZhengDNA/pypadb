import pymysql
from dbutils.pooled_db import PooledDB

import configurer

POOL = None


def init_pool():
    global POOL
    POOL = PooledDB(
        creator=pymysql,

    )
