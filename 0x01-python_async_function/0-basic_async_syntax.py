#!/usr/bin/env python3
'''0-basic_async_syntax.py file
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''asynchronous coroutine(wait_random)
    takes max_delay: int argument default value 10
    waits for a random delay btwn 0 - max_delay
    return random delay value: float
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
