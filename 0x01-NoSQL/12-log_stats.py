#!/usr/bin/env python3
"""
Write a Python script that provides some stats
about Nginx logs stored in MongoDB:
    - Database: logs
    - Collection: nginx
"""


def main():
    """
    Enry Point
    """
    from pymongo import MongoClient
    import pprint
    client = MongoClient()
    db = client['logs']
    nginx = db['nginx']
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    print("{} logs".format(nginx.count_documents({})))

    pipeline = [
        {"$match": {"$or": [{"method": "GET"}, {"method": "POST"}, {
            "method": "PUT"}, {"method": "PATCH"}, {"method": "DELETE"}]}},
        {"$group": {"_id": "$method", "count": {"$sum": 1}}}
    ]
    result = list(nginx.aggregate(pipeline))
    print("Methods:")
    for method in methods:
        count = 0
        f_result = list(filter(lambda x: x['_id'] == method, result))
        if f_result:
            count = f_result[0]['count']
        print("\tmethod {}: {}".format(method, count))
    pipeline = [
        {"$match": {"$and": [{"method": "GET"}, {"path": "/status"}]}},
        {"$group": {"_id": None, "count": {"$sum": 1}}}
    ]
    result = list(nginx.aggregate(pipeline))
    if result:
        print("{} status check".format(result[0].get('count', 0)))


if __name__ == '__main__':
    main()
