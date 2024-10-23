# 0x02. Redis basic
## Resources
### Read or watch:
- [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)
- [Redis commands](https://redis.io/docs/latest/commands/)
- [Redis python client](https://redis-py.readthedocs.io/en/stable/)
- [How to Use Redis With Python](https://realpython.com/python-redis/)

## What is Redis?: An Overview
- Redis is an open source data structure server. It belongs to the class of NoSQL databases known as key/value stores. Keys are unique identifiers, whose value can be one of the data types that Redis supports. These data types range from simple Strings, to Linked Lists, Sets and even Streams. Each data type has its own set of behaviours and commands associated with it.
- For example, I can store my name in a Redis String and associate it with the key "myname" using a Redis SET command. I can then retrieve the value using a Redis GET command. Here's how that looks using redis-cli, a command line interface to Redis:
```
127.0.0.1:6379> set myname "Simon Prickett"
OK
127.0.0.1:6379> get myname
"Simon Prickett"
```
- Keys in a Redis database are distributed in a flat keyspace. Redis does not enforce a schema or naming policy for keys. This provides great flexibility, with the organization of the keyspace being the responsibility of the developer.
- Redis is famous for being an extremely fast database. This speed comes from the fact that it stores and serves all data from memory rather than disk. Redis is durable, so your data will be persisted, but all reads will be from a copy of the data held in memory. This makes Redis an excellent choice for applications that require real time data access.
- Redis is also often used as a cache, and has specific functionality to support this. Redis can be extended with new functionality using plugin modules. We'll see how to use some of these as we make our way through the course.