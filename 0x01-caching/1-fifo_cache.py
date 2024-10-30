#!/usr/bin/env python3
'''FIFO caching'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''FIFOCache class'''
    def __init__(self):
        '''Inilialize'''
        super().__init__()

    def put(self, key, item):
        '''store item that have key-value pairs'''
        if key is not None or item is not None:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = next(iter(self.cache_data))
                del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")
        self.cache_data[key] = item

    def get(self, key):
        '''return the value from cache_data'''
        if key in None or key not in self.cache_data:
            return None
        return self.cache_data[key]
