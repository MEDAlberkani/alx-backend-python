#!/usr/bin/env python3
import asyncio
import time
#from concurrent_coroutines import wait_n

wait_n = __import__('concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n

n = 5
max_delay = 9

print(measure_time(n, max_delay))
