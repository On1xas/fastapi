from abc import ABC, abstractmethod
from redis import Redis


class RedisAbstrastRepository(ABC):

    @abstractmethod
    async def get_key():
        raise NotImplementedError

    @abstractmethod
    async def set_key():
        raise NotImplementedError


class RedisDB(RedisAbstrastRepository):
    redis: Redis = None
    
    async def get_key(self, key_name):
        result = self.redis.get(key_name)
        return result

    async def set_key(self, key_name,  value):
        self.redis.set(name=key_name, value=value)