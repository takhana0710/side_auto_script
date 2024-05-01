from testcase.gpg2_chromeset import driver_eng, gpg_api,ma_api,env
import logging
"""
1.後台搜尋會員然後都把它找出來＋代理
2.前台登入取token
3.開始轉蛋
"""
get_info = 'Activity/Drawlots/2022WhiteDay/GetSpins'
free = 'Activity/Drawlots/2022WhiteDay/Spin/free'
paid = 'Activity/Drawlots/2022WhiteDay/Spin/paid'
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M', handlers=[logging.FileHandler(
    'my.log', 'w', 'utf-8')])
magpg = ma_api() # 後台ＡＰＩ
res = magpg.apiGetData(method='get', api_url=env['back_api'] + 'Member/MemberList',
                       payload={'IsFuzzySearch': True, 'PhoneNumber': '+886  9', 'Skip': 0, 'Show': 50,
                                'Field': 'CreateTime', 'OrderType': 'desc', 'IsGuest': False})['Data']  # 搜尋全部測試帳號
def spin(account):
    driver = driver_eng()  # 前台瀏覽器
    driver.loginV2(phone=account,validcode='  ',passredis=True)
    api = gpg_api(token=driver.token)
    res = api.apiGetData(method='get',payload={},api_url=env['font_api']+get_info).get('Data')
    print(api.apiGetData(method='post', payload={}, data={}, api_url=env['font_api'] + free).get('Data')) # 單次
    print(api.apiGetData(method='post', payload={}, data={}, api_url=env['font_api'] + paid).get('Data')) # 單次
    # for _ in range(res.get('FreeRemains')):
    #     print(api.apiGetData(method='post', payload={},data={},api_url=env['font_api'] + free).get('Data'))
    # for _ in range(res.get('PaidRemains')):
    #     print(api.apiGetData(method='post', payload={},data={},api_url=env['font_api'] + paid).get('Data'))
    # driver.cleanRedis()

list(map(lambda x:spin(x.get('PhoneNumber')),res))
    
    



