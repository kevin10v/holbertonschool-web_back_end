#!/usr/bin/env python3
"""Function that sums a mixed list of integers and floats."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum all integers and floats in a list and return the total.

    Args:
        mxd_lst: List containing integers and/or floats

    Returns:
        Sum of all numbers as a float
    """
    return sum(mxd_lst)
