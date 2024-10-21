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
    for method in methods:
        count = 0
        f_result = list(filter(lambda x: x['_id'] == method, result))
        if f_result:
            count = f_result[0]['count']
        print("    method {}: {}".format(method, count))


if __name__ == '__main__':
    main()
