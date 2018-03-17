import time
import asyncio
import aiohttp
import datetime
import math

count = 0
loop = asyncio.get_event_loop()


async def display_date(l, number):
    end_time = l.time() + 5.0
    while (l.time()) <= end_time:
        t = end_time - l.time()
        await asyncio.sleep(1)
        print('task : ', number, ' count : ', math.floor(6 - t), datetime.datetime.now())


async def timer(l, m):
    fs = [display_date(l, x) for x in range(m)]

    await asyncio.wait(fs)
    print('done')


# Blocking call which returns when the display_date() coroutine is done
loop.run_until_complete(timer(loop, 5))

loop.close()