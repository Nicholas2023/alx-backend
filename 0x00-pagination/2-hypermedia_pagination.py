#!/usr/bin/env python3
"""
A module that implements class Server
"""
import csv
import math
from math import ceil
from typing import List, Dict

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
    Server to paginate a database of popular
    baby name
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Amethod that initializes the data set
        """
        self._dataset = None

    def dataset(self) -> List[List]:
        """
        Cached data set
        """
        if self._dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self._dataset = dataset[1:]

        return self._dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get page content from csv file
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        range_index = index_range(page, page_size)
        start_index = range_index[0]
        end_index = range_index[1]
        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        A method that give hypermedia pagination
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        range_index = index_range(page, page_size)
        start_index = range_index[0]
        end_index = range_index[1]
        data_page = self.get_page(page, page_size)
        full_data = self.dataset()
        total_pages = ceil(len(full_data) / page_size)

        dict1 = {
            "page_size": len(data_page),
            "page": page,
            "data": data_page,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
        return dict1
