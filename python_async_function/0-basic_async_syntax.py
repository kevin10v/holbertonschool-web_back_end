#!/usr/bin/env python3
"""Module for basic async syntax with random delay."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay.

    Args:
        max_delay: Maximum delay in seconds (default 10)

    Returns:
        The actual random delay time as a float between 0 and max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
