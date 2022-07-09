# -*- coding:utf-8 -*-
# @Author     : Yushuo
# @CreateTime : 2022/7/9 18:35
from redis import Redis, ConnectionPool

redis_pool = ConnectionPool(host='127.0.0.1', port=6379, db=0)


class RedisUtil:
    """
    Redis 操作工具类
    """
    @staticmethod
    def get_connection():
        return Redis(connection_pool=redis_pool, decode_responses=True)


if __name__ == '__main__':
    conn = RedisUtil.get_connection()
    # conn.set('name', 'zhangsan', ex=10)
    print(conn.get('name'))

