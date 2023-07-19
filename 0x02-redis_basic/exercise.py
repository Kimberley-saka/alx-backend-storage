#!/usr/bin/env python3
"""
Redis
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class, stores an instance of the redis client
    flushes the instance using flushdb
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generates a random key
        """
        key = str(uuid.uuid4())
        if isinstance(data, (str, bytes, int, float)):
            self._redis.set(key, data)
        return key
