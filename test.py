import asyncio
import aiohttp as aiohttp


async def start_client(url):

    session = aiohttp.ClientSession()
    async with session.ws_connect(url) as ws:

        async for msg in ws:
            print(msg.json())
            if msg.type == aiohttp.WSMsgType.TEXT:
                if msg.data == 'close cmd':
                    await ws.close()
                    break
                else:
                    await ws.send_str('{"op": "subscribe", "args": ["orderBookL2:XBTUSD"]}')
            elif msg.type == aiohttp.WSMsgType.CLOSED:
                break
            elif msg.type == aiohttp.WSMsgType.ERROR:
                break


if __name__ == '__main__':
    wsUrl = 'wss://www.bitmex.com/realtime'

    loop = asyncio.get_event_loop()
    loop.create_task(start_client(wsUrl))
    loop.run_forever()