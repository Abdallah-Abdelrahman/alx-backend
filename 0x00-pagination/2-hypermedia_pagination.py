#!/usr/bin/env python3
'''Module defines `index_range` function and `Server` class'''
import csv
import math
from typing import Dict, List, Tuple


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
        '''Initialze the instance'''
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
        '''returns paginated dataset'''
        assert isinstance(page, int) and page > 0\
            and isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if end >= len(dataset) or start >= len(dataset):
            # out of range pagination
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''hypermeid as the engine of application state.

        Returns:
            dictionary with the following keys:
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        '''
        prev_page = None
        next_page = None
        data = self.get_page(page, page_size)

        if page > 1:
            prev_page = page - 1
        if len(data) > 0:
            next_page = page + 1

        return {
                'page_size': page_size if len(data) > 0 else 0,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': math.ceil(len(self.__dataset)/page_size),
        }
