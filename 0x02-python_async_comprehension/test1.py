#!/usr/bin/env python3

import asyncio
async def test(): 
    return [i async for i in range(100) if i % 2]
loop = asyncio.get_event_loop()
loop.run_until_complete(test())
