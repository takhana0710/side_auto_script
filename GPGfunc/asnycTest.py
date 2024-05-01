import aiohttp
from aiohttp import ClientSession
import asyncio
import redis
# from testcase.gpg2_chromeset import driver_eng
from testcase.magpg_chormeset import ma_api
api=ma_api()
data = api.apiGetData(method='get',api_url='',
                      payload={'IsFuzzySearch': True,'Skip': 0,'Show': 50,'Field': 'CreateTime',"OrderType": 'desc',
                                                                                               'IsGuest': False,'PhoneNumber': '+88699999997'})['Data']
res = list(map(lambda i:i.get('PhoneNumber'),data))

r = redis.Redis(host='localhost', port=6379, db=3,decode_responses=True)
async def main():
    async with ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session :
        task = [asyncio.create_task(req(session,i)) for i in res]
        tasks =  [asyncio.create_task(sign(session,i)) for i in res]
        await asyncio.gather(*task,*tasks)

async def req(session,account):
    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'authorization': 'Bearer %s' % r.get(account)
    }
    async with session.get('',headers =header) as res:
        response = await res.json()
        # print(response)


async def sign(session,account):
    header = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'authorization': 'Bearer %s' % r.get(account)
    }
    async with session.post('',json={"Month":"2022-01"},headers=header) as res:
        response = await res.json()
        print(response)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
