#!/usr/bin/env python3

import asyncio
import random


async def wait_random(max_delay = 10):
    if not (isinstance(max_delay, (int, float))):
        return
    results = random.uniform(0, max_delay)
    await asyncio.sleep(results)
    return results
