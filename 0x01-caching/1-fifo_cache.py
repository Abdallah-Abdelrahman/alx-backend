#!/usr/bin/env python3
'''Module defines `FIFOCache` class'''
from typing import Any, Union
from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    '''caching using FIFO algorithm'''
    def __init__(self) -> None:
        '''Initialze the instance'''
        super().__init__()
        self.queue = deque()

    def put(self, key: str, item: Any) -> None:
        '''put a value in the cache'''
        if key and item:
            if key in self.cache_data:
                # key already exist
                # don't change order
                self.cache_data[key] = item
                self.queue.remove(key)
                self.queue.append(key)
                return
            if len(self.cache_data) >= self.MAX_ITEMS:
                k = self.queue.popleft()
                del self.cache_data[k]
                print('DISCARD: {}'.format(k))
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key) -> Union[None, Any]:
        '''retrieve value from cache'''
        return self.cache_data.get(key)
