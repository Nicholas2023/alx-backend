#!/usr/bin/env python3
"""
A module that implements the class MRUCache()
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Defines cache system based on MRU algorithm
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add items in cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                mru_key = self.queue.pop()
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """
        Get an item based on its key
        """
        if key is not None and key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
