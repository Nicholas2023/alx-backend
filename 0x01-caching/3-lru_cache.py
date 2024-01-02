#!/usr/bin/env python3
"""
A module that implements the class LRUCache()
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    A class that defines a cache system based on LRU
    algorithm
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                lru_key = self.queue.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
