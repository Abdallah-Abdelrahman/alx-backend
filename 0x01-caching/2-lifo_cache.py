#!/usr/bin/env python3
'''Module defines `LIFOCache` class'''
from typing import Any, Union
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''caching using LIFO algorithm'''
    def __init__(self):
        '''Initialze the instance'''
        super().__init__()
        self.stack = []

    def put(self, key: str, item: Any):
        '''put a value in the cache'''
        if key and item:
            if key in self.cache_data:
                # key already exist
                # rearrange order
                self.cache_data[key] = item
                self.stack.remove(key)
                self.stack.append(key)
                return
            if self.MAX_ITEMS == len(self.cache_data):
                k = self.stack.pop()
                del self.cache_data[k]
                print('DISCARD: '.format(k))
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key: str) -> Union[None, Any]:
        '''retrieve value from cache'''
        return self.cache_data.get(key)
