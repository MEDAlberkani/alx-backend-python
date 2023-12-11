#!/usr/bin/env python3
import asyncio
from typing import List 
from heapq import nsmallest
from wait_random import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = await asyncio.gather(*[wait_random(max_delay) for i in range(n)])
    return sorted(delays)

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
