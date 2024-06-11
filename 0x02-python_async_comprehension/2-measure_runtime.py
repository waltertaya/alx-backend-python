#!/usr/bin/env python3
"""
This module contains a coroutine to measure
the runtime of executing async comprehensions in parallel.
"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime - function execute async_com 4 times
    Arguments:
        no arguments
    Returns:
        the total exection time required to complete the task
    """
    time_start = time.perf_counter()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    time_end = time.perf_counter()
    return (time_end - time_start)