import asyncio
import aiohttp


    async def start_client(url):

        session = aiohttp.ClientSession()
        async with session.ws_connect(url) as ws:

            async for msg in ws:

                # Connected
                if msg.type == aiohttp.WSMsgType.TEXT:

                    json_msg = msg.json()
                    # First connection message
                    if 'version' in json_msg and 'limit' in json_msg:

                        if json_msg['limit']['remaining'] > 0:
                            await ws.send_str('{"op": "subscribe", "args": ["trade:XBTUSD"]}')
                        else:
                            # Error
                            print(json_msg)

                    else:
                        # Print result
                        print(json_msg)
                elif msg.type == aiohttp.WSMsgType.CLOSED:
                    break
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    break


if __name__ == '__main__':
    wsUrl = 'wss://www.bitmex.com/realtime'

    loop = asyncio.get_event_loop()
    loop.create_task(start_client(wsUrl))
    loop.run_forever()
