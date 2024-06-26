#!/usr/bin/env python3
'''Module defines `LRUCache` class'''
from typing import Any, Union
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    '''caching using Least Recent Used algorithm'''
    def __init__(self):
        '''Initialze the instance'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key: str, item: Any) -> None:
        '''put a value in the cache'''
        if key and item:
            if key in self.cache_data:
                # key already exist
                # rearrange order
                self.cache_data[key] = item
                self.cache_data.move_to_end(key)
                return
            if len(self.cache_data) >= self.MAX_ITEMS:
                k, _ = self.cache_data.popitem(last=False)
                print('DISCARD: {}'.format(k))
            self.cache_data[key] = item

    def get(self, key: str) -> Union[None, Any]:
        '''retrieve value from cache'''
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
