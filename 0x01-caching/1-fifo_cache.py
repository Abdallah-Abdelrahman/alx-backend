#!/usr/bin/env python3
'''Module defines `FIFOCache` class'''
from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    '''caching using FIFO algorithm'''
    def __init__(self):
        '''Initialze the instance'''
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        '''put a value in the cache'''
        if key and item:
            if key in self.cache_data:
                # key already exist
                # don't change order
                self.cache_data[key] = item
                return
            if self.MAX_ITEMS == len(self.cache_data):
                k = self.queue.popleft()
                del self.cache_data[k]
                print('DISCARD: ', k)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        '''retrieve value from cache'''
        return self.cache_data.get(key)
