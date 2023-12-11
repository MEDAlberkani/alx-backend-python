#!/usr/bin/env python3
import random
import asyncio

async def wait_random(max_delay: int = 10):
    random_no = random.uniform(0, max_delay)
    await asyncio.sleep(random_no)
    return random_no

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
