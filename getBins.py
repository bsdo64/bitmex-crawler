import asyncio
import aiohttp
import pandas as pd
import time
import pyqtgraph


async def start_client(end_point, params_dic):
    async with aiohttp.ClientSession() as session:
        async with session.get(end_point, params=params_dic) as resp:
            df = pd.read_json(await resp.text())
            # print(resp.status)
            print(resp.headers["x-ratelimit-remaining"])
            print(df.dtypes)


if __name__ == '__main__':
    FIRST_DATE_SECONDS = 1483228800  # 2017-01-01 utc
    m = (time.time() - FIRST_DATE_SECONDS) / 60

    baseUrl = 'https://www.bitmex.com/api/v1/'
    endpoint = 'trade/bucketed'
    params = {
        "binSize": "1m",
        "symbol": 'XBTUSD',
        "columns": "symbol,timestamp,close,high,lastSize,low,open,volume,trades",
        "count": 500,
        "start": 0,
        "reverse": 'true'
    }
    requestUrl = baseUrl + endpoint

    tasks = []
    loop = asyncio.get_event_loop()

    for x in range(0, 60):
        tasks.append(start_client(requestUrl, params))

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
