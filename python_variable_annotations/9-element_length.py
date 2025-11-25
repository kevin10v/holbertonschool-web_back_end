#!/usr/bin/env python3
"""Function that returns list of tuples with sequence lengths."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return list of tuples containing each element and its length.

    Args:
        lst: Iterable of sequences (strings, lists, tuples, etc.)

    Returns:
        List of tuples with (sequence, length)
    """
    return [(i, len(i)) for i in lst]
