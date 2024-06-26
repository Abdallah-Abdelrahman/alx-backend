#!/usr/bin/env python3
'''Module defines `LIFOCache` class'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''caching using LIFO algorithm'''
    def __init__(self):
        '''Initialze the instance'''
        super().__init__()
        self.stack = []

    def put(self, key, item):
        '''put a value in the cache'''
        if key and item:
            if key in self.cache_data:
                # key already exist
                # don't change order
                self.cache_data[key] = item
                self.stack.remove(key)
                self.stack.append(key)
                return
            if self.MAX_ITEMS == len(self.cache_data):
                k = self.stack.pop()
                del self.cache_data[k]
                print('DISCARD: ', k)
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        '''retrieve value from cache'''
        return self.cache_data.get(key)
