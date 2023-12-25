#!/usr/bin/env python3
"""
A module that implements the index_range()
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates start and end indices for pagination
    Args:
        page (int): The page number (1-indexed)
        page_size (int): the number of items per page
    Returns:
        Tuple[int, int]: A tuple containing the start and end
        indices. The indices are zero-based
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
