"""
Remember to use asyncio.run() to actually force execution 
by scheduling the main() coroutine (future object) 
for execution on the event loop:
"""
import asyncio

async def main():
     print("Hello ...")
     await asyncio.sleep(1)
     print("World!")

routine = main()
routine # <coroutine object main at 0x1027a6150>
asyncio.run(routine)
