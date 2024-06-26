#!/usr/bin/env python3
'''Module defines `MRUCache` class'''
from typing import Any, Union
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    '''caching using Most Recent Used algorithm'''
    def __init__(self):
        '''Initialze the instance.

        Note:
            the `OrderedDict` DS behaves like LIFO and FIFO,
            when removing we remove from end(MRU),
            when updating or accessing element,
            it's shifted to the end as well.
        '''
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
                k, _ = self.cache_data.popitem()
                print('DISCARD: {}'.format(k))
            self.cache_data[key] = item

    def get(self, key: str) -> Union[None, Any]:
        '''retrieve value from cache'''
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
