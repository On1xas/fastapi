from src.db.db import redis_tools
from src.utils.redis_repository import RedisDB


class RedisRepository(RedisDB):
    def __init__(self):
        self.redis = redis_tools
