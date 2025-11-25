#!/usr/bin/env python3
"""Module for measuring async execution time."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure total execution time for wait_n and return average time per call.

    Args:
        n: Number of times to spawn wait_random
        max_delay: Maximum delay for each wait_random call

    Returns:
        Average time per operation (total_time / n)
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
