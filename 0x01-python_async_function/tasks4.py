#!/usr/bin/env python3
import asyncio
from typing import List
from heapq import nsmallest

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    delays = await asyncio.gather(*[task_wait_random(max_delay) for i in range(n)])
    return sorted(delays)

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
