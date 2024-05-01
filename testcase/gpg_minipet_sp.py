import struct
import time
import websockets
import certifi
import re
import ssl
import json
import asyncio
url='wss://mkqa-pet-connector.ceis.tw/'
ssl_context=ssl.create_default_context()
ssl_context.load_verify_locations(certifi.where())
"""
2022/12/28 mining pet spider ver 1.0
2023/01/09 mining pet spider ver 1.0 done for some main logic function
"""
def main_hash(**kwargs):
    """
    :param kwargs:
    {"send":{"order":1,"info":b'',"hash":">4h","routeCode":"int"}}
    :return:
    {"res_hash":res_hash,"recv_order":recv_order}
    """
    data = kwargs.get('data')
    """
    加密規則：
    (1024,封包長度(標頭4byte+內容),請求順序,routeCode)封包內容
    """
    # print(len(data['send']['info']))
    # print(data['send']['order'],data['send']['info'])
    res_hash=struct.pack(">4h",1024,len(data['info'])+4,data['order'],data['routeCode'])+data['info']
    recv_order = 1024+(data['order']-256)
    send_order=data['order']+1
    return {"res_hash":res_hash,"recv_order":recv_order,'send_order':send_order}

async def send(**kwargs):
    info=kwargs.get('info')
    order=kwargs.get('order')
    recv_count = kwargs.get('recv_count')
    routeCode=kwargs.get('routeCode')
    websocket=kwargs.get('websocket')
    # is_while_loop = kwargs.get('is_while_loop')
    data = {}
    data['info'] = bytes(json.dumps(info, separators=(',', ':')), encoding='utf-8')
    try:
        data['routeCode'] = routeCode['sys']['routeToCode'][info['__route__']]
    except:
        data['routeCode'] = routeCode['sys']['routeToCode'][info['route']] # 特殊處理使用道具
    data['order'] = order
    res = main_hash(data=data)
    data['order'] = res['send_order']  # 打完一包更新發送順序
    print(res['res_hash'])
    time.sleep(2)
    await websocket.send(res['res_hash'])
    # print(res['res_hash'])
    get_data = {}
    count = 0
    # recv = await websocket.recv()
    while True:
        try:
            # http://shouce.jb51.net/python-3.9.0a2/library/asyncio-task.html
            # 註記一下可能的為啥的版本差異
            recv = await asyncio.wait_for(websocket.recv(), timeout=5)
            print(recv)
            head = struct.Struct('>3h')
            head_decode = head.unpack_from(recv[:head.size])
            if res['recv_order'] == head_decode[2]:
                js_data = json.loads(recv[head.size:].decode('utf-8'))
                get_data={'info': js_data,'order':data['order']}
                return get_data
        except asyncio.TimeoutError:
            print('確定收完封包')
            break
        except:
            count+=1
            if count>10:
                break
            pass

async def login(websocket,token):
    await websocket.send(b'\x01\x00\x00\x4b{"sys":{"type":"js-websocket","version":"0.0.1","rsa":{},"protoVersion":0}}')
    recv = await websocket.recv()
    routeCode = re.compile(b'.*?({"code":200,"sys":{.*?}})',re.S).findall(recv).pop()
    routeCode = json.loads(routeCode.decode('utf-8'))
    info = {"uid":"test0864","access_token":token,"token":"","dc":"GPG","lang":"tw","browserType":"chrome","browserVersion":"108.0.0.0","os":"OS X","osVersion":"","isMobile":'false',"__route__":"connector.connectorHandler.login","msg":'null'}
    await websocket.send(b'\x02\x00\x00\x00')
    get_user_info= await send(info=info,order=257,recv_count=2,routeCode=routeCode,websocket=websocket)
    return get_user_info,routeCode

async def common(websocket,info,routeCode):
    user_info = info
    data = await send(info={"__route__": "mainLogic.mainLogicHandler.getFrienzList", "query": {}},order=user_info['order'], recv_count=1, routeCode=routeCode, websocket=websocket)
    data = await send(info={"__route__":"mainLogic.mainLogicHandler.getCommonCostData","query":{"uid":user_info['info']['msg']['uid']}},order=data['order'],recv_count=1,routeCode=routeCode,websocket=websocket)
    data = await send(info={"__route__": "mainLogic.mainLogicHandler.getBagList", "query": {}}, order=data['order'],recv_count=1, routeCode=routeCode, websocket=websocket)
    data = await send(info={"__route__": "mainLogic.mainLogicHandler.getPetList", "query": {}}, order=data['order'],recv_count=1, routeCode=routeCode, websocket=websocket)
    data = await send(info={"__route__": "mainLogic.mainLogicHandler.getGamesData"}, order=data['order'], recv_count=1,routeCode=routeCode, websocket=websocket)
    data = await send(info={"__route__": "mainLogic.mainLogicHandler.getPromosData"}, order=data['order'], recv_count=1,routeCode=routeCode, websocket=websocket)
    data = await send(info={"__route__": "mainLogic.mainLogicHandler.getMailList", "query": {"nowPage": 1}},order=data['order'], recv_count=1, routeCode=routeCode, websocket=websocket)
    return data
    
async def qr_step(websocket,info,routeCode,mk_item):
    data=info
    data = await send(info={"__route__": "mainLogic.mainLogicHandler.debugSendMail", "query": {"id": mk_item, "quota": 1}}, order=data['order'],recv_count=2, routeCode=routeCode, websocket=websocket)
    mail_info = await send(info={"__route__": "mainLogic.mainLogicHandler.getMailList", "query": {"nowPage": 1}},order=data['order'], recv_count=1, routeCode=routeCode, websocket=websocket)
    qr_item = list(filter(lambda x:x.get('gId')==mk_item,mail_info['info']['data']['list'])).pop()
    data = await send(info={"__route__":"mainLogic.mainLogicHandler.getOneMail","query":{"mailId":qr_item['mId']}},order=mail_info['order'], recv_count=1, routeCode=routeCode, websocket=websocket)
    data = await send(info={"__route__":"mainLogic.mainLogicHandler.getOneMailAnnex","query":{"mailId":qr_item['mId']}}, order=data['order'],recv_count=2, routeCode=routeCode, websocket=websocket)
    bag_info = await send(info={"__route__": "mainLogic.mainLogicHandler.getBagList", "query": {}}, order=data['order'],recv_count=1, routeCode=routeCode, websocket=websocket)
    item_id = list(filter(lambda x: x.get('iId') == mk_item, bag_info['info']['data']['list'])).pop()  # 使用實體核銷券
    data = await send(info={"route":"mainLogic.mainLogicHandler.useItem","query":{"useId":item_id['_id'],"quota":1,"useQuota":None,"useMId":None,"mIdx":None}}, order=bag_info['order'],recv_count=1, routeCode=routeCode, websocket=websocket)
    url = data['info']['data']['couponOrderUrl']
    return url

async def useItem(**kwargs): # 使用東西
    token = kwargs.get('token')
    async with websockets.connect(url, ssl=ssl_context) as websocket:
        get_user_info, routeCode = await login(websocket, token)
        data = await common(websocket=websocket, info=get_user_info, routeCode=routeCode)
        bag_info = await send(info={"__route__": "mainLogic.mainLogicHandler.getBagList", "query": {}},order=data['order'], recv_count=1, routeCode=routeCode, websocket=websocket)


async def get_mail(**kwargs): # 取得信件
    token = kwargs.get('token')
    async with websockets.connect(url,ssl=ssl_context) as websocket:
        get_user_info, routeCode = await login(websocket,token)
        data = await common(websocket=websocket,info=get_user_info,routeCode=routeCode)
        return data['info']

async def retail_red_coffee(**kwargs):
    token = kwargs.get('token')
    async with websockets.connect(url,ssl=ssl_context) as websocket:
        get_user_info, routeCode = await login(websocket,token)
        data = await common(websocket=websocket,info=get_user_info,routeCode=routeCode)
        await qr_step(websocket=websocket,info=data,routeCode=routeCode,mk_item=16050)

async def newPlayLesson(websocket,info,routeCode):
    get_user_info=info
    data = await send(info={"__route__": "mainLogic.mainLogicHandler.getFrienzList", "query": {}},order=get_user_info['order'], recv_count=1, routeCode=routeCode, websocket=websocket)
    data = await send(info={"__route__": "mainLogic.mainLogicHandler.getCommonCostData","query": {"uid": get_user_info['info']['msg']['uid']}}, order=data['order'], recv_count=1,routeCode=routeCode, websocket=websocket)
    bag_info = await send(info={"__route__": "mainLogic.mainLogicHandler.getBagList", "query": {}}, order=data['order'],recv_count=1, routeCode=routeCode, websocket=websocket)
    data = await send(info={"__route__": "mainLogic.mainLogicHandler.getPetList", "query": {}}, order=bag_info['order'],recv_count=1, routeCode=routeCode, websocket=websocket)
    data = await send(info={"__route__": "mainLogic.mainLogicHandler.getGamesData"}, order=data['order'], recv_count=1,routeCode=routeCode, websocket=websocket)
    data = await send(info={"__route__": "mainLogic.mainLogicHandler.getPromosData"}, order=data['order'], recv_count=1,routeCode=routeCode, websocket=websocket)
    data = await send(info={"__route__": "mainLogic.mainLogicHandler.getMailList", "query": {"nowPage": 1}},order=data['order'], recv_count=1, routeCode=routeCode, websocket=websocket)
    data = await send(info={"__route__": "mainLogic.mainLogicHandler.getQuestsData", "query": {}}, order=data['order'],recv_count=1, routeCode=routeCode, websocket=websocket)
    data = await send(info={"__route__": "mainLogic.mainLogicHandler.setMiningPet","query": {"mId": 10, "pId": 1001, "pIdx": 0, "isSetOn": 'true'}}, order=data['order'],recv_count=2, routeCode=routeCode, websocket=websocket)
    data = await send(info={"__route__": "mainLogic.mainLogicHandler.startOneMining","query": {"minesId": get_user_info['info']['msg']['uid'] + "_10"}}, order=data['order'],recv_count=3, routeCode=routeCode, websocket=websocket)
    """設定完小雞等著加速"""
    black_cow = list(filter(lambda x: x.get('iId') == 10003, bag_info['info']['data']['list'])).pop()  # 神牛加速
    data = await send(info={"route": "mainLogic.mainLogicHandler.useItem","query": {"useId": black_cow['_id'], "quota": 1, "useQuota": 1, "useMId": 10, "mIdx": 0}},order=data['order'], recv_count=3, routeCode=routeCode, websocket=websocket)
    data = await send(info={"__route__": "mainLogic.mainLogicHandler.finishOneMining","query": {"minesId": get_user_info['info']['msg']['uid'] + "_10", "moneyType": "GPGG"}},order=data['order'], recv_count=4, routeCode=routeCode, websocket=websocket)
    bag_info = await send(info={"__route__": "mainLogic.mainLogicHandler.getBagList", "query": {}}, order=data['order'],recv_count=1, routeCode=routeCode, websocket=websocket)
    bart = list(filter(lambda x: x.get('iId') == 10008, bag_info['info']['data']['list'])).pop()  # 巴特兌換券
    data = await send(info={"route": "mainLogic.mainLogicHandler.useItem","query": {"useId": bart['_id'], "quota": 1, "useQuota": 'null', "useMId": None,"mIdx": None}}, order=bag_info['order'], recv_count=2, routeCode=routeCode,websocket=websocket)
    data = await send(info={"__route__": "mainLogic.mainLogicHandler.getPetList", "query": {}}, order=data['order'],recv_count=1, routeCode=routeCode, websocket=websocket)
    data = await send(info={"__route__": "mainLogic.mainLogicHandler.setMiningPet","query": {"mId": 10, "pId": 2001, "pIdx": 1, "isSetOn": 'true'}}, order=data['order'],recv_count=2, routeCode=routeCode, websocket=websocket)
    data = await send(info={"__route__": "mainLogic.mainLogicHandler.startOneMining","query": {"minesId": get_user_info['info']['msg']['uid'] + "_10"}}, order=data['order'],recv_count=3, routeCode=routeCode, websocket=websocket)
    data = await send(info={"route": "mainLogic.mainLogicHandler.useItem","query": {"useId": black_cow['_id'], "quota": 1, "useQuota": 1, "useMId": 10, "mIdx": 0}},order=data['order'], recv_count=2, routeCode=routeCode, websocket=websocket)
    data = await send(info={"__route__": "mainLogic.mainLogicHandler.finishOneMining","query": {"minesId": get_user_info['info']['msg']['uid'] + "_10", "moneyType": "GPGG"}},order=data['order'], recv_count=3, routeCode=routeCode, websocket=websocket)

async def singlePool(**kwargs):
    token = kwargs.get('token')
    async with websockets.connect(url, ssl=ssl_context) as websocket:
        get_user_info, routeCode = await login(websocket, token)
        data = await newPlayLesson(websocket=websocket, info=get_user_info, routeCode=routeCode)
        # return data['info']

async def draw(**kwargs):
    token = kwargs.get('token')
    async with websockets.connect(url,ssl=ssl_context) as websocket:
        get_user_info, routeCode = await login(websocket,token)
        data = await common(websocket=websocket,info=get_user_info,routeCode=routeCode)
        await qr_step(websocket=websocket,info=data,routeCode=routeCode,mk_item=16050)

async def MiningMainStart(**kwargs):
    token = kwargs.get('token') # token 必填
    new_player = kwargs.get('new_player') # 預設 None 代表不是新手 {"check_mail":bool}
    mini = kwargs.get('mini') # 預設 None 代表不處理 dict {"count":int} # 要挖多少次
    use_item = kwargs.get('use_item') # dict {"item_id":int,"exchange":bool}
    async with websockets.connect(url,ssl=ssl_context) as websocket:
        get_user_info, routeCode = await login(websocket,token)
        if new_player == None:
            data = await common(websocket=websocket,info=get_user_info,routeCode=routeCode)
        else:
            data = await newPlayLesson(websocket=websocket, info=get_user_info, routeCode=routeCode)
        if mini != None:
            count = mini['count']
            data = await send(info={"__route__": "mainLogic.mainLogicHandler.debugSendMail", "query": {"id": 10002, "quota": count}},order=data['order'], recv_count=2, routeCode=routeCode, websocket=websocket)
            mail_info = await send(info={"__route__": "mainLogic.mainLogicHandler.getMailList", "query": {"nowPage": 1}},order=data['order'], recv_count=1, routeCode=routeCode, websocket=websocket)
            item = mail_info['info']['data']['list'][0]
            data = await send(info={"__route__": "mainLogic.mainLogicHandler.getOneMail", "query": {"mailId": item['mId']}},order=mail_info['order'], recv_count=1, routeCode=routeCode, websocket=websocket)
            data = await send(info={"__route__": "mainLogic.mainLogicHandler.getOneMailAnnex", "query": {"mailId": item['mId']}},order=data['order'], recv_count=1, routeCode=routeCode, websocket=websocket)
            bag_info = await send(info={"__route__": "mainLogic.mainLogicHandler.getBagList", "query": {}},order=data['order'], recv_count=1, routeCode=routeCode, websocket=websocket)
            item_mid = list(filter(lambda x: x.get('iId') == 10002, bag_info['info']['data']['list'])).pop()  # 黑牛加速
            for _ in range(count):
                data = await send(info={"__route__": "mainLogic.mainLogicHandler.startOneMining","query": {"minesId": get_user_info['info']['msg']['uid'] + "_10"}},order=data['order'], recv_count=2, routeCode=routeCode, websocket=websocket)
                data = await send(info={"route":"mainLogic.mainLogicHandler.useItem","query":{"useId":item_mid,"quota":1,"useQuota":1,"useMId":10,"mIdx":0}},order=data['order'], recv_count=1, routeCode=routeCode, websocket=websocket)
                data = await send(info={"__route__": "mainLogic.mainLogicHandler.finishOneMining","query": {"minesId": get_user_info['info']['msg']['uid'] + "_10","moneyType": "GPGG"}}, order=data['order'], recv_count=3,routeCode=routeCode, websocket=websocket)
                data = await send(info={"__route__": "mainLogic.mainLogicHandler.getBagList", "query": {}},order=data['order'], recv_count=1, routeCode=routeCode, websocket=websocket)
        if use_item != None:
            pass
        
        

