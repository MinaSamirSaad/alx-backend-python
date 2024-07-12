#!/usr/bin/env python3
'''Task 0's module.
'''
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    '''Takes an integer max_delay and returns a random float
    that is the result of the function wait_random.
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
