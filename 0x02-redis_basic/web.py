#!/usr/bin/env python3
"""
web.py
"""
import requests
import redis
from typing import Callable
from functools import wraps


def cach_result(func: Callable) -> Callable:
    """
    cach decorator
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        url: str = ""
        if args:
            url = args[0]
        elif kwargs and 'url' in kwargs:
            url = kwargs['url']
        if url:
            r = redis.Redis(decode_responses=True)
            result = r.get(url)
            if result:
                return result
            result = func(*args, **kwargs)
            r.set(url, result)
            r.expire(url, 10)
            return result
    return wrapper


def count_url(func: Callable) -> Callable:
    """
    count url request
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        url: str = ""
        if args:
            url = args[0]
        elif kwargs and 'url' in kwargs:
            url = kwargs['url']
        if url:
            r = redis.Redis(decode_responses=True)
            r.incr("count:{}".format(url))
        return func(*args, **kwargs)
    return wrapper


@count_url
@cach_result
def get_page(url: str) -> str:
    """
    obtain the HTML content of a particular URL and returns it.
    """
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        return response.text


if __name__ == '__main__':
    url = "http://slowwly.robertomurray.co.uk"
    r = redis.Redis(decode_responses=True)
    result = get_page(url)
    print("{}:{}".format(r.get("count:{}".format(url)), url))
    get_page(url)
    print("{}:{}".format(r.get("count:{}".format(url)), url))
    get_page(url)
    print("{}:{}".format(r.get("count:{}".format(url)), url))
    get_page(url)
    print("{}:{}".format(r.get("count:{}".format(url)), url))
    get_page(url)
    print("{}:{}".format(r.get("count:{}".format(url)), url))
