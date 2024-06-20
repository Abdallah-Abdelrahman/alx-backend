#!/usr/bin/env python3
'''Module defines `index_range` function'''
import csv
import math
from typing import List, Tuple, Union


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''returns range of indexes.
    to return in a list for those particular pagination parameters
    '''
    return ((page - 1) * page_size, page * page_size)


class Server:
    '''Server class to paginate a database of popular baby names.
    '''
    DATA_FILE = 'Popular_Baby_Names.csv'

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        '''Cached dataset
        '''
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0\
                and isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if end >= len(dataset) or start >= len(dataset):
            # out of range pagination
            return []

        return [dataset[i] for i in range(start, end)]
