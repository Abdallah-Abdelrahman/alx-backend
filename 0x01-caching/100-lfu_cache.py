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
        self.occurence = {}

    def put(self, key: str, item: Any) -> None:
        '''put a value in the cache'''

        if key and item:
            if not self.occurence.get(key):
                self.occurence[key] = 0
            self.occurence[key] += 1

            if key in self.cache_data:
                # key already exist
                # rearrange order
                self.cache_data[key] = item
                self.cache_data.move_to_end(key)
                return

            if len(self.cache_data) >= self.MAX_ITEMS:
                lfu = {}
                for k, v in self.occurence.items():
                    if v not in lfu:
                        lfu[v] = []
                    lfu[v].append(k)
                print(lfu)
                min_ = min(lfu.keys())
                if len(lfu[min_]) == 1:
                    # perform LFU replcement
                    self.cache_data.pop([lfu[min_]])
                    print('DISCARD: {}'.format(lfu[min_]))
                else:
                    # perform LRU replacement
                    k, _ = self.cache_data.popitem(last=False)
                    print('DISCARD: {}'.format(k))
            self.cache_data[key] = item

    def get(self, key: str) -> Union[None, Any]:
        '''retrieve value from cache'''
        if key in self.cache_data:
            self.occurence[key] += 1
            self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
