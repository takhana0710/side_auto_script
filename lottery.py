from testcase.gpg2_chromeset import BackAPI,ma_api,env
import time
import random
import requests
import websockets
import certifi
import ssl
import asyncio

url=''
ssl_context=ssl.create_default_context()
ssl_context.load_verify_locations(certifi.where())
phone=""
requests.post(url=f'{env["play_api"]}Token/ValidateContactInfo',json={"Phone":phone})
requests.post(url=f'{env["play_api"]}Token/SendLoginVerification',json={"Phone":phone})
res = ma_api().apiGetData(method='get',api_url=BackAPI.infos_smsVerifications.value)
verifycode=list(filter(lambda x:x.get('Phone')==phone,res['Data']))[0]['Code']
lottery_token = requests.post(url=f'{env["play_api"]}connect/token',
                              headers={"Content-Type":"application/x-www-form-urlencoded"},
                              data={"client_id": "mark_six","client_secret": "4fypra!c!?",
                                    "grant_type": "mk_phone","phone":phone,"verifycode": verifycode}).json()
print(lottery_token)
ws_login ={"cmd":"ln","data":{"account":"","gameId":"","key":lottery_token['access_token']}}
numbers = random.sample(range(1, 50), 6)
print(numbers)
async def lottery():
   async with websockets.connect(url,ssl=ssl_context) as websocket:
    await websocket.send(str(ws_login))
    res = await websocket.recv()
    print(res)
    data = {"cmd":"bet","data":{"betCode":numbers}}
    print(str(data))
    await websocket.send(str(data))
    bet_res = await websocket.recv()
    print('======')
    print(bet_res)
    websocket.close()
asyncio.get_event_loop().run_until_complete(lottery())