#!/usr/bin/env python3
'''FIFO caching'''
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    '''FIFOCache class'''
    def __init__(self):
        '''Inilialize'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''store item that have key-value pairs'''
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.cache_data.popitem(False)
            print(f"DISCARD:", first_key)

    def get(self, key):
        '''return the value from cache_data'''
        return self.cache_data.get(key, None)
