import requests
from testcase.gpg2_chromeset import TransferDict # 錢包enum
import hashlib
import json
from script.utils import TimeSelect
time_select = TimeSelect()
def verifyCode():
    url = '  /Token/AdLogin'
    res = requests.post(url, json={"account": "QAminiag21","password": "QAminiag21","reCAPTCHA": "string"}).json()
    print(res)
    return res['code']
token_url = '  /connect/token'
ptid = TransferDict.gpg_silver.value
def SingleWalletSearch():
    access_token,client_id = m2mToken()
    url = '  SingleWallet/Search'
    data={
      "PointTypeID": ptid,
      "MemberID": 2353
    }
    data['sign']=mdValue(data,client_id)
    print('======>data',data)
    print(requests.get(url, headers={'Authorization': f'Bearer {access_token}'}, params=data).status_code)
    print(requests.get(url, headers={'Authorization': f'Bearer {access_token}'}, params=data).text)
def mdValue(value,client_id):
    m=hashlib.md5()
    res = json.dumps(value, sort_keys=True)
    # print(str(res).replace(',','&'))
    mdbefore = ''
    for k, v in json.loads(res).items():
        a = str(k) + '=' + str(v) + '&'
        mdbefore = mdbefore + a
    mk_key=f'{client_id}apiKey'
    print('==========>',mdbefore[:-1]+mk_key)
    m.update((mdbefore[:-1]+mk_key).encode('utf-8'))
    return m.hexdigest()

def m2mToken():
    grant_type='client_credentials'
    if grant_type=='client_credentials':
        client_id = "mk1"
        data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": "secret",
        # "scope": {"mining.sharedpool.search", "singlewallet.search"},
        }
    else:
        client_id = "mk"
        data = {
            "grant_type": "mk_adLogin",
            "client_id": client_id,
            "client_secret": "secret",
            "scope": {"mining.sharedpool.search", "singlewallet.search"},
            "code":verifyCode()
        }
    res = requests.post(url=token_url, data=data)
    print(res.text)
    print(res.status_code)
    access_token = res.json()['access_token']
    return access_token,client_id
def MiningPoolPublic():
    access_token,client_id = m2mToken()
    url = '  Mining/pool/public'
    month = time_select.MonthEnd()[:7]  # ex:2022-05
    data={
      "Date": month
    }
    data['sign']=mdValue(data,client_id)
    print('======>data',data)
    print(requests.get(url, headers={'Authorization': f'Bearer {access_token}'}, params=data).status_code)
    print(requests.get(url, headers={'Authorization': f'Bearer {access_token}'}, params=data).text)
