#!/usr/bin/env python3
"""
This module contains a coroutine to measure
the runtime of executing async comprehensions in parallel.
"""

import asyncio
import time
from typing import List
async_comprehension = __import__('1_async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing
    async_comprehension four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """

    t_start = time.perf_counter()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    t_end = time.perf_counter()
    return (t_end - t_start)
