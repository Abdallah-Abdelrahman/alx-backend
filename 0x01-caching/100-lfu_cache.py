#!/usr/bin/env python3
'''Module defines `LFUCache` class'''
from typing import Any, Union
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    '''caching using Least Frequently Used algorithm'''
    def __init__(self):
        '''Initialze the instance

        Note:
            the `OrderedDict` DS behaves like LIFO and FIFO,
            when removing we remove from left(LRU),
            when updating or accessing element,
            it's shifted to the end (MRU)
        '''
        super().__init__()
        self.cache_data = OrderedDict()
        self.used_count = {}

    def put(self, key: str, item: Any) -> None:
        '''put a value in the cache'''

        if key is None or item is None:
            return

        # If the key already exists, update the item and use count
        if key in self.cache_data:
            self.cache_data[key] = item
            self.used_count[key] += 1
            self.cache_data.move_to_end(key)
            return

        # If the cache is full, remove the least frequently used item
        if len(self.cache_data) >= self.MAX_ITEMS:
            lfu_key = min(self.used_count,
                          key=lambda k: (self.used_count[k], k))
            self.cache_data.pop(lfu_key)
            self.used_count.pop(lfu_key)
            print('DISCARD: {}'.format(lfu_key))

        # Add the new item and set its use count to 1
        self.cache_data[key] = item
        self.used_count[key] = 1

    def get(self, key: str) -> Union[None, Any]:
        '''retrieve value from cache'''
        if key in self.cache_data:
            self.used_count[key] += 1
            self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
