#!/usr/bin/env python3
import asyncio

wait_random = __import__('basic_async_syntax').wait_random


def  task_wait_random(max_delay: int) -> asyncio.Task:
    task1 = asyncio.create_task(wait_random(max_delay))
    return task1

async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
