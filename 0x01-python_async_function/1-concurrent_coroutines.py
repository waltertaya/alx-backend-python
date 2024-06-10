#!/usr/bin/env python3
'''1-concurrent_coroutines.py file
'''

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    '''Implements wait_n async routine
    Args: n -> int, max_delay -> int
    Body: spawn wait_random n times with the specified max_delay
    Return: list of the all the delays(float values)
    '''
    response_list = []
    for i in range(n):
        response_list.append(await wait_random(max_delay))
    return response_list
