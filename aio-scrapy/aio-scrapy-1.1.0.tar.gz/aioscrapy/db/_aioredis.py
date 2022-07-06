from redis.asyncio import BlockingConnectionPool, Redis

from aioscrapy.db.absmanager import AbsDBPoolManager


class RedisExecutor:

    def __init__(self, alias: str, pool_manager: "AioRedisPoolManager"):
        self.alias = alias
        self.pool_manager = pool_manager

    def __getattr__(self, command):
        redis_pool: Redis = self.pool_manager.get_pool(self.alias)
        return getattr(redis_pool, command)


class AioRedisPoolManager(AbsDBPoolManager):
    _clients = {}

    async def create(self, alias: str, params: dict) -> Redis:
        if alias in self._clients:
            return self._clients[alias]

        params = params.copy()
        url = params.pop('url', None)
        params.setdefault('socket_connect_timeout', 30)
        if url:
            connection_pool = BlockingConnectionPool.from_url(url, **params)
        else:
            connection_pool = BlockingConnectionPool(**params)
        redis = Redis(connection_pool=connection_pool)
        return self._clients.setdefault(alias, redis)

    def get_pool(self, alias: str):
        """获取数据库链接和数据库游标"""
        redis_pool: Redis = self._clients.get(alias)
        assert redis_pool is not None, f"redis没有创建该连接池： {alias}"
        return redis_pool

    def executor(self, alias: str) -> RedisExecutor:
        return RedisExecutor(alias, self)

    async def close(self, alias: str):
        """关闭指定redis pool"""
        redis = self._clients.pop(alias, None)
        if redis:
            await redis.close()
            await redis.connection_pool.disconnect()

    async def close_all(self):
        for alias in list(self._clients.keys()):
            await self.close(alias)

    async def from_dict(self, db_args: dict):
        for alias, redis_args in db_args.items():
            await self.create(alias, redis_args)

    async def from_settings(self, settings: "aioscrapy.settings.Setting"):
        for alias, redis_args in settings.getdict('REDIS_ARGS').items():
            await self.create(alias, redis_args)


redis_manager = AioRedisPoolManager()


if __name__ == '__main__':
    import asyncio


    async def test():
        await redis_manager.create('default', {
            'url': 'redis://@192.168.234.128:6379/9',
        })
        redis = redis_manager.executor('default')
        print(await redis.zadd('key1', {'value': 2}))

        async with redis.pipeline(transaction=True) as pipe:
            results, count = await (
                pipe.zrange('key1', 0, 0)
                    .zremrangebyrank('key1', 0, 0)
                    .execute()
            )

        print(results)
        await redis_manager.close_all()


    # asyncio.run(test())
    asyncio.get_event_loop().run_until_complete(test())
