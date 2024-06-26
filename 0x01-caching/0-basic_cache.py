#!/usr/bin/env python3
'''Module defines `BasicCache` '''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''caching system '''
    def put(self, key, item):
        '''put a value in the cache'''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        '''retrieve value from cache'''
        return self.cache_data.get(key)
