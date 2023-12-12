#!/usr/bin/env python3
"""
A coroutine that will execute async_comprehension
4times using asyncio.gather
"""

import asyncio
from typing import Generator
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of async_comprehension four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    start = time.time()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    end = time.time()
    return end - start
