#!/usr/bin/env python3
"""Function that returns a tuple with string and squared number."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple with a string and the square of a number.

    Args:
        k: String key
        v: Integer or float value

    Returns:
        Tuple containing the string k and v squared as float
    """
    return (k, v ** 2)
