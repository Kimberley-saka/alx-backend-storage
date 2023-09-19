#!/usr/bin/env python3
"""
Insert documents based on **kwargs
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """inserts a new document"""
    return mongo_collection.insert(kwargs)
