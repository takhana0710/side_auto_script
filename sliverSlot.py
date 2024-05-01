from testcase.gpg2_chromeset import ma_api,BackAPI
api=ma_api()
data = api.apiGetData(method='get',api_url='',
                      payload={'IsFuzzySearch': True,'Skip': 0,'Show': 50,'Field': 'CreateTime',"OrderType": 'desc', 'IsGuest': False,'PhoneNumber': ''})['Data']

# data = api.apiGetData(method='get',api_url='',
#                       payload={'IsFuzzySearch': True,'Skip': 0,'Show': 50,'Field': 'CreateTime',"OrderType": 'desc','IsGuest': False})['Data']
# res = list(filter(lambda x:x.get('PhoneNumber') == '',data)).pop()
res = list(map(lambda i:i.get('MemberID'),data))
print(res)
# res = []
# print('====>',api.apiGetData(method='post',api_url=BackAPI.member_disable.value,data={"MemberId":}))
[api.apiGetData(method='post',api_url='',data={"MemberId":i}) for i in res]