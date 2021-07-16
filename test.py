import asyncio
import aiohttp
import time
URL = 'http://localhost:8080'
requests_list = [
                    '/price/BTC', '/price/ETH', '/price/BTC', '/price/ETH',
                    '/price/history/?page=2',
                    '/price/BTC', '/price/ETH', '/price/BTC', '/price/ETH',
                    '/price/BTC', '/price/ETH', '/price/BTC', '/price/ETH',
                    '/price/history/?page=1',
                    '/price/BTC', '/price/ETH', '/price/BTC', '/price/ETH',
                    '/price/BTC', '/price/ETH', '/price/BTC', '/price/ETH',
]


def test_tasks(session):
    tasks = []
    for req in requests_list:
        tasks.append(session.get(URL+req, ssl=False))
    return tasks


async def testing():
    async with aiohttp.ClientSession() as session:
        tasks = test_tasks(session)
        ress = await asyncio.gather(*tasks)
        for res in ress:
            print(await res.json(content_type=None))


start = time.time()
asyncio.run(testing())
print(abs(start-time.time()))
