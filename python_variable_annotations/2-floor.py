#!/usr/bin/env python3
"""Function that returns the floor of a float."""
import math


def floor(n: float) -> int:
    """Return the floor of a float.

    Args:
        n: Float number to floor

    Returns:
        Largest integer not greater than n
    """
    return math.floor(n)
