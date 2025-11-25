#!/usr/bin/env python3
"""Module for executing multiple tasks concurrently."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with specified max_delay.

    Args:
        n: Number of tasks to create
        max_delay: Maximum delay for each task_wait_random call

    Returns:
        List of delays in ascending order without using sort()
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        # Insert delay in correct position to maintain ascending order
        inserted = False
        for i in range(len(delays)):
            if delay < delays[i]:
                delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            delays.append(delay)

    return delays
