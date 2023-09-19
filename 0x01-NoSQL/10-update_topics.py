#!/usr/bin/env python3
"""
Change topic
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """changes all topics"""
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
