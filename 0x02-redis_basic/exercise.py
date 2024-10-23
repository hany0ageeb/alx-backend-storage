#!/usr/bin/env python3
"""
- Create a Cache class.
- In the __init__ method,
- store an instance of the Redis client as a private variable
named _redis (using redis.Redis()) and flush the instance
using flushdb.
- Create a store method that takes a data argument and
returns a string.
- The method should generate a random key (e.g. using uuid),
- store the input data in Redis using
the random key and return the key.
- Type-annotate store correctly.
Remember that data can be a str, bytes, int or float.
"""
import redis
import uuid
from typing import Union, Callable, Any


class Cache:
    """
    Cache class.
    """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        takes a data argument and returns a string.
        should generate a random key (e.g. using uuid)
        store the input data in Redis
        return the key
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Union[Callable[[bytes], Any], None] = None) -> Any:
        """
        take a key string argument and an optional Callable argument named fn
        This callable will be used to convert
        the data back to the desired format.
        """
        value = self._redis.get(key)
        if fn and value:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        wrapper that call self.get and convert to str
        """
        return self.get(key, lambda value: value.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        wrapper that call self.get and convert to int
        """
        return self.get(key, lambda value: int(value))
