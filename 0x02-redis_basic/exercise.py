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
from functools import wraps


def replay(method: Callable) -> None:
    """
    display the history of calls of a particular function.
    """
    r = redis.Redis(decode_responses=True)
    key = method.__qualname__
    call_count = r.get(key)
    print("{} was called {} times:".format(key, call_count))
    inputs = r.lrange("{}:inputs".format(key), 0, -1)
    outputs = r.lrange("{}:outputs".format(key), 0, -1)
    for in_out in zip(inputs, outputs):
        print("{}(*({},)) -> {}".format(key, in_out[0], in_out[1]))


def count_calls(method: Callable) -> Callable:
    """
    As a key, use the qualified name of method
    using the __qualname__ dunder method.
    Create and return function that increments the count
    for that key every time the method is called
    and returns the value returned by the original method.
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        args[0].incr(method.__qualname__)
        return method(*args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    call_history
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        inputs = [str(arg) for arg in args[1:]] + \
            [v for k, v in kwargs.items() if k != 'self']
        args[0].rpush("{}:inputs".format(method.__qualname__), *inputs)
        output = [method(*args, **kwargs)]
        args[0].rpush("{}:outputs".format(method.__qualname__), *output)
        return output
    return wrapper


class Cache:
    """
    Cache class.
    """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

    def incr(self, key: str) -> None:
        """
        wrapper around Redis.incr method
        """
        self._redis.incr(key)

    def rpush(self, name: str, *args) -> None:
        """Wrapper around Redis.rpush"""
        self._redis.rpush(name, *args)
