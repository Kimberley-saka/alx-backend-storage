#!/usr/bin/env python3
"""
List documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """List documents in s collection"""
    if not mongo_collection:
        return []
    docs = mongo_collection.find()
    return [doc for doc in docs]
