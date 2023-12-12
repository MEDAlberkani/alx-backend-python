#!/usr/bin/env python3
"""
A coroutine that takes no arguments
imported from async_generator
"""

from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """
    Yields 10 random numbers.
    """
    g = [i async for i in async_generator()]
    return g
