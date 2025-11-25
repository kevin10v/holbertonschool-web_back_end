#!/usr/bin/env python3
"""Function that sums a list of floats."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum all floats in a list and return the total.

    Args:
        input_list: List of float numbers

    Returns:
        Sum of all floats in the list
    """
    return sum(input_list)
