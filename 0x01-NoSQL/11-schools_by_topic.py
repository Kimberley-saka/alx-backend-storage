#!/usr/bin/env python3
"""
Returns list of schools having specific topic
"""
def schools_by_topic(mongo_collection, topic):
    """returns the list of schools"""
    return mongo_collection.find({"topics": topic})
