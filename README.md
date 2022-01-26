## pypadb

对 Mybatis 的拙劣模仿

目前只支持了 MySQL

使用了 pydantic，预计还会用 SQLAlchemy，学习中。

[使用文档](https://chenzdna.github.io/tag/pypadb/)

### install

`pip install pypadb`

### Usage

#### select

```python
from pydantic import BaseModel

from conf.db_configurer import DbConfigurer
from decorator.select import select


class User(BaseModel):
    id: int
    account: str


@select('select * from user', data_type=User)
def get_sth_many() -> list[User]:
    pass


@select('select * from user where id = %(id)s', data_type=User)
def get_sth_one(id: int) -> User:
    pass


if __name__ == '__main__':
    # end() must be called
    DbConfigurer() \
        .set_host('localhost') \
        .set_user('root') \
        .set_password('123456') \
        .set_database('test') \
        .end()

    print(get_sth_many())
    # [User(...), User(...), ...]
    print(get_sth_one(1))
    # id=1 account='...'
```

另一种方法

```python
from pydantic import BaseModel

from conf.db_configurer import db_configurer
from conf.table_configurer import tables
from utils.conditions import Like, Limit
from utils.enums import LikeEnum


class User(BaseModel):
    id: int
    account: str


class Stuff(BaseModel):
    name: str
    count: int


if __name__ == '__main__':
    db_configurer \
        .set_host('localhost') \
        .set_user('root') \
        .set_password('123456') \
        .set_database('test') \
        .end()
    # init tables
    tables.init_tables(user=User, stuff=Stuff)
    print(
        tables.user.select_many(limit=Limit(1))
    )
    # [User(id=1, account='123456')]
    print(
        tables.user.select_many(limit=Limit(0, 3))
    )
    # [User(id=1, account='123456'), User(id=2, account='123454563466'), User(id=3, account='12gsdfhs')]
    print(
        tables.user.select_like(likes=Like('account', '123', LikeEnum.R_Like))
    )
    # Like(column, value, like_mode)
    # argument likes: Union[list[Like], Like]
    # print result [User(id=1, account='123456'), User(id=2, account='123454563466')]
```
