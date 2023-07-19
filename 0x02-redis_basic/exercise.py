#!/usr/bin/env python3
"""
Redis
"""
import redis
import uuid
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable = None) ->
    /Union[str, bytes, int, None]:
        """
        converts the data back to the desired format
        """
        data = self._redis.get(key)
        if data is None:
            return None

        if fn is None:
            return data

        return fn(data)

    def get_str(self, key: str) -> Union[str, None]:
        """
        automatically parametrize Cache.get with the correct
        conversion function
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        automatically parametrize Cache.get with the correct
        conversion function
        """
        return self.get(key, fn=lambda d: int(d))
