#!/usr/bin/env python3
"""
Write a Python function that returns all students sorted by average score:
Prototype: def top_students(mongo_collection):
mongo_collection will be the pymongo collection object
The top must be ordered
The average score must be part of each item returns with key = averageScore
"""
import pymongo
import pymongo.collection


def top_students(mongo_collection: pymongo.collection.Collection):
    """
    returns all students sorted by average score
    """
    pipeline = [
        {
            "$unwind": "$topics"
        },
        {
            "$group": {
                "_id": "$name",
                "averageScore": {
                    "$avg": "$topics.score"
                },
                "s_d": {
                    "$addToSet": "$_id"
                }
            }
        },
        {
            "$sort": {"averageScore": -1}
        },
        {
            "$project": {
                "_id": {"$arrayElemAt": ["$s_d", 0]},
                "name": "$_id",
                "averageScore": 1
            }
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
