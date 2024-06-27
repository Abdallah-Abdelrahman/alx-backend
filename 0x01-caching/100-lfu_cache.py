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
            it's used to retain the order of insertion.
        '''
        super().__init__()
        self.cache_data = OrderedDict()
        self.used_count = {}

    def put(self, key: str, item: Any) -> None:
        '''put a value in the cache'''

        if key and item:
            if key in self.cache_data:
                # key already exist (cache hit)
                # rearrange order
                self.cache_data[key] = item
                self.used_count[key] += 1
                return

            if len(self.cache_data) >= self.MAX_ITEMS:
                # max hit
                lfu = {}
                for k, v in self.used_count.items():
                    if v not in lfu:
                        lfu[v] = []
                    lfu[v].append(k)

                k = lfu[min(lfu.keys())][0]  # LRU when there's a tie
                self.cache_data.pop(k)
                self.used_count.pop(k)
                print('DISCARD: {}'.format(k))
            self.cache_data[key] = item
            self.used_count[key] = 1

    def get(self, key: str) -> Union[None, Any]:
        '''retrieve value from cache'''
        if key in self.cache_data:
            self.used_count[key] += 1
        return self.cache_data.get(key)
