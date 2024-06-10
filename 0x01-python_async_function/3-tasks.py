#!/bin/usr/env python3
''' 3-tasks.py file
'''

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    ''' Implements task_wait_random function
    Args: max_delay: int
    Returns: asyncio.Task
    '''
    loop = asyncio.get_event_loop()
    return loop.create_task(wait_random(max_delay))
