import asyncio

async def mygen(u: int = 10):
     """Yield powers of 2."""
     i = 0
     while i < u:
         yield 2 ** i
         i += 1
         await asyncio.sleep(0.1)
