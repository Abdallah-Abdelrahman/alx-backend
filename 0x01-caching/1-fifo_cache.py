#!/usr/bin/env python3
'''Module defines `FIFOCache` class'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''caching using FIFO algorithm'''
    def put(self, key, item):
        '''put a value in the cache'''
        if key and item:
            if self.MAX_ITEMS == len(self.cache_data):
                k = next(iter(self.cache_data))
                self.cache_data.pop(k)
                print('DISCARD: ', k)
            self.cache_data[key] = item

    def get(self, key):
        '''retrieve value from cache'''
        return self.cache_data.get(key)
