#!/usr/bin/env python3
"""
Write a Python function that returns the list of school
having a specific topic:
    - Prototype: def schools_by_topic(mongo_collection, topic):
    - topic (string) will be topic searched
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic
    """
    return mongo_collection.find({"topics": {"$all": [topic]}})
