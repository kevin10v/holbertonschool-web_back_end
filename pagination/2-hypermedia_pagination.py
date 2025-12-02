#!/usr/bin/env python3
"""Hypermedia pagination module."""

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing start and end indexes for pagination.

    Args:
        page: The current page number (1-indexed).
        page_size: The number of items per page.

    Returns:
        A tuple of (start_index, end_index) for the given page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server instance."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of the dataset.

        Args:
            page: The page number (1-indexed), default is 1.
            page_size: The number of items per page, default is 10.

        Returns:
            A list of rows for the requested page, or empty if out of range.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Return hypermedia pagination information.

        Args:
            page: The page number (1-indexed), default is 1.
            page_size: The number of items per page, default is 10.

        Returns:
            A dictionary containing pagination information:
            - page_size: the length of the returned dataset page
            - page: the current page number
            - data: the dataset page
            - next_page: number of the next page, None if no next page
            - prev_page: number of the previous page, None if no previous page
            - total_pages: the total number of pages in the dataset
        """
        data = self.get_page(page, page_size)
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

