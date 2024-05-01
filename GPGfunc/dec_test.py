from testcase.gpg2_chromeset import driver_eng, gpg_api
import pymongo
import redis
import uuid
apiUrl = ''
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

sys_dict = {'ag_acc': 'rrrrrr', 'ag_psw': 'rrrrrr', 'friend_id': 2972, 'Phone': '+', 'PackageID': 10122,
            'AcceptPromotion': '42czmf0'}
apiInfo = [
    {'method': 'get', 'path': '/Member/MemberInfo', 'payload': None, 'data': None},
    {'method': 'get', 'path': '/Chat/ChatRoomList', 'payload': None, 'data': None},
    {'method': 'get', 'path': '/Friend/FriendList', 'payload': None, 'data': None},
    {'method': 'get', 'path': '/Member/MemberWallet', 'payload': None, 'data': None},
    {'method': 'get', 'path': '/Wallet/Search','payload': {"PointTypeID": 1, "CheckProviderMember": True, "UpdateFromProvider": True},'data': None},
    {'method': 'get', 'path': '/Game/HomeBanner', 'payload': None, 'data': None},
    {'method': 'get', 'path': '/Game/HomeHotGame', 'payload': None, 'data': None},
    {'method': 'get', 'path': '/Game/GameList', 'payload': None, 'data': None},
    {'method': 'get', 'path': '/Activity/NoviceSignIn7thList', 'payload': None, 'data': None},
    {'method': 'get', 'path': '/Activity/NoviceSignIn7th', 'payload': None, 'data': None},
    {'method': 'get', 'path': '/ElectronicMall/PackageList', 'payload': {"PaymentType": 1}, 'data': None},
    {'method': 'get', 'path': '/Member/PhoneAvailability', 'payload': None, 'data': None},
    {'method': 'post', 'path': '/Transaction/SendTransactionPasswordVerify', 'payload': None, 'data': {}},
    {'method': 'get', 'path': '/Mining/MonsterBackpack', 'payload': None, 'data': None},
    {'method': 'get', 'path': '/Mining/MinerlMonsterInfo', 'payload': None, 'data': None},
    {'method': 'post', 'path': '/Mining/MinerlMonsterTreasure', 'payload': None, 'data': None},
    {'method': 'post', 'path': '/Mining/ElfTreasure', 'payload': None, 'data': None},
    {'method': 'post', 'path': '/Member/AddNickname', 'payload': None, 'data': {"Nickname": "QAAAuto"}},
    {'method': 'post', 'path': '/Member/Nickname', 'payload': None, 'data': {"Nickname": "QAAAuto"}},
    {'method': 'get', 'path': '/Game/GameLink','payload': {'PointTypeID': 1, 'GameID': 5, 'GameProvider': 'VA', 'GameProviderGameID': 24,'ReturnUrl': '  5', 'Lang': 'zh-TW'}, 'data': None},
    {'method': 'post', 'path': '/Member/UpdateMemberStatus', 'payload': None, 'data': {"GameID": 0}},
    {'method': 'post', 'path': '/Wallet/TransferRecord', 'payload': None,'data': {"PointTypeID": 0, "FromWalletID": -1, "ToWalletID": -1, "sDate": "2021-11-08T10:20:39+08:00","eDate": "2021-12-09T10:20:39+08:00", "Skip": 0, "Show": 1000, "Field": "CreateTime","OrderType": "desc"}},
    {'method': 'post', 'path': '/Wallet/Transfer', 'payload': None,'data': {"FromWalletPointTypeID": 1, "ToWalletPointTypeID": 220101, "Point": 1, "CheckProviderMember": True}},
    {'method': 'post', 'path': '/Transaction/CheckTransactionPasswordVerify', 'payload': None,'data': {"VerifyCode": "345345"}},
    {'method': 'post', 'path': '/Transaction/VerifyPassword', 'payload': None,'data': {"TransactionPassword": "123456"}},
    {'method': 'post', 'path': '/Transaction/EstimateFee', 'payload': None, 'data': {"Point": 1000}},
    {'method': 'post', 'path': '/Transaction/SubmitRewardPoint', 'payload': None,'data': {"PointTypeID": 1, "Point": 1000, "TransactionPassword": "123456"}},
    {'method': 'post', 'path': '/Transaction/discloseSerialNo', 'payload': None, 'data': {"TID": 557}},
    {'method': 'post', 'path': '/Chat/InitUnReadCount', 'payload': None,'data': {"GroupID": sys_dict.get('friend_id')}},
    {'method': 'post', 'path': '/Chat/SendChatText', 'payload': None,'data': {"GroupID": sys_dict.get('friend_id'), "Content": "567565"}},
    {'method': 'post', 'path': '/ElectronicMall/BuyPackage', 'payload': None,'data': {"PackageID": sys_dict.get("PackageID"), "UniformInvoiceInfo": {"DonateMark": 0, "NPOBAN": "919"}}},
    {'method': 'post', 'path': '/Member/UpdateAvatarFrame', 'payload': None, 'data': {"HeadPhotoFrameID": 18}},
    {'method': 'post', 'path': '/Token/CreateGuest', 'payload': None,'data': {"UUID": str(uuid.uuid4()), "Device": "Macintosh, Chrome"}},
    {'method': 'post', 'path': '/Member/CertifiedPhone', 'payload': None, 'data': {"VerifyCode": "999999"}},
    {'method': 'post', 'path': '/Member/AcceptPromotion', 'payload': None,'data': {"PromoteCode": sys_dict.get('AcceptPromotion')}},
    {'method': 'post', 'path': '/Member/AcceptPromotion', 'payload': None,'data': {"AvatarID": "  /Avatar/2.jpg"}},
    {'method': 'get', 'path': '/Friend/SearchFriend', 'payload': {"SearchKeyword": 'QQAACC'}, 'data': None},
    {'method': 'post', 'path': '/Friend/FriendAdd', 'payload': None,'data': {"FriendID": sys_dict.get('friend_id')}},
    {'method': 'get', 'path': '/Chat/ChatRoomText','payload': {'GroupID': sys_dict.get('friend_id'), 'Skip': 0, 'Show': 100}, 'data': None},
    {'method': 'get', 'path': '/Chat/ChatGroup', 'payload': {"FriendID": 23}, 'data': None},
    {'method': 'get', 'path': '/Transaction/SetTransactionPassword', 'payload': {"TransactionPassword": "123456"},'data': None},
    {'method': 'get', 'path': '/Transaction/TransactionRecord','payload': {'StartDate': '2021-11-30T16:00:00.000Z', 'EndDate': '2021-12-09T15:59:59.999Z', 'RecordType': 2,'Skip': 0}, 'data': None},
    {'method': 'get', 'path': '/Game/RecommendGame', 'payload': None, 'data': None},
    {'method': 'get', 'path': '/Game/GameInfo', 'payload': {"GameID": 5}, 'data': None},
    {'method': 'get', 'path': '/Member/AvatarFrameRepository', 'payload': None, 'data': None},
    {'method': 'get', 'path': '/Member/AvatarRepository', 'payload': None, 'data': None},
    {'method': 'get', 'path': '/Member/OrderList','payload': {'StartDate': '2021-11-30T16:00:00.000Z', 'EndDate': '2021-12-09T15:59:59.999Z'}, 'data': None},
    {'method':'post','path':'/wallet/TransferBack','payload':None,'data':{"PointTypeID":1}}
]

def dec_guest(func):
    def decorator():
        if r.get('guesttoken') == None:
            driver = driver_eng()
            driver.guest()
            r.set('guesttoken',driver.token)
            func(driver.token)
        else:
            func(r.get('guesttoken'))
    return decorator

def dec_member(func):
    def decorator():
        if r.get('membertoken') == None:
            driver = driver_eng()
            driver.loginV2()
            r.set('membertoken',driver.token)
            func(driver.token)
        else:
            func(r.get('membertoken'))
    return decorator

def dec_agent(func):
    def decorator():
        if r.get('agenttoken') == None:
            driver = driver_eng()
            driver.loginV2()
            r.set('agenttoken',driver.token)
            func(driver.token)
        else:
            func(r.get('agenttoken'))
    return decorator

@dec_guest
def guest(token):
    api=gpg_api(token=token)
    list(map(lambda x:api.apiGetData(method=x['method'],payload=x['payload'],api_url=apiUrl+x['path'],data=x['data']), apiInfo))


@dec_member
def member(token):
    api=gpg_api(token=token)
    list(map(lambda x:api.apiGetData(method=x['method'],payload=x['payload'],api_url=apiUrl+x['path'],data=x['data']), apiInfo))

@dec_agent
def agent(token):
    api=gpg_api(token=token)
    list(map(lambda x:api.apiGetData(method=x['method'],payload=x['payload'],api_url=apiUrl+x['path'],data=x['data']), apiInfo))

@dec_agent
def agent(token):
    api=gpg_api(token=token)
    list(map(lambda x:api.apiGetData(method=x['method'],payload=x['payload'],api_url=apiUrl+x['path'],data=x['data']), apiInfo))
guest()
print('----------------訪客測試完成------------------')
member()
print('----------------會員測試完成------------------')
agent()
print('----------------代理會員測試完成------------------')

