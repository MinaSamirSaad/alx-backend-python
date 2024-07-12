#!/usr/bin/env python3
'''Task 4's module.
'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Takes an integer n and an integer max_delay as arguments
    that waits for a random delay between 0 and max_delay
    using the function wait_random n times, then returns a list
    of the delays.
    '''
    delays = [task_wait_random(max_delay) for _ in range(n)]
    return sorted([await delay for delay in asyncio.as_completed(delays)])
