#!/usr/bin/env python3
"""Function that returns a multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function that multiplies a float by multiplier.

    Args:
        multiplier: The multiplier value

    Returns:
        A function that takes a float and returns it multiplied
    """
    def multiplier_func(value: float) -> float:
        """Multiply value by multiplier."""
        return value * multiplier

    return multiplier_func
