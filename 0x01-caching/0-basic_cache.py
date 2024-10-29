#!/usr/bin/env python3
'''module for caching file'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''bashcache that inherits from basecaching'''
    def __init__(self):
        '''Initilliaze'''
        super().__init__()
    
    def put(self, key, item):
        '''Store key-value pair in the cache_data dictionary'''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''return value of self.cache_data linked to the key'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
