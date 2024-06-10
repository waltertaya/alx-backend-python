#!/usr/bin/env python3
'''1-concurrent_coroutines.py file
'''

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Implements wait_n async routine
    Args: n -> int, max_delay -> int
    Body: spawn wait_random n times with the specified max_delay
    Return: list of all the delays (float values)
    '''
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
