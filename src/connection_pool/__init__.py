from typing import Union

from dbutils.pooled_db import PooledDB, PooledDedicatedDBConnection, PooledSharedDBConnection

import exception

_POOL: PooledDB = None


def _init_pool(data: dict):
    global _POOL
    _POOL = PooledDB(**data)


def get_connection() -> Union[PooledSharedDBConnection, PooledDedicatedDBConnection]:
    if not _POOL:
        raise exception.PoolUninitializedException('connection pool uninitialized')
    return _POOL.connection()
