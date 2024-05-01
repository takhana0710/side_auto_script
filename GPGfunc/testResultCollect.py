from lxml import etree
import re
import pymongo
import requests
# version = driver_eng(headless=True).version()
client = pymongo.MongoClient('127.0.0.1', 27017)

def Read(**kwargs):
    db = client['automation']
    col = db['testResult']
    report = db['testReport']
    with open(kwargs.get('file'),'r',encoding='utf-8') as f:
        html=etree.HTML(f.read().encode('utf-8'))
        f.close()
    res = html.xpath('//table[@id="result_table"]/tr')
    now = html.xpath('//div[@class="heading"]/p[2]//text()')[1].lstrip()
    total = html.xpath('//div[@class="heading"]/p[3]//text()')[1].lstrip()
    result = html.xpath('//div[@class="heading"]/p[4]//text()')[1].lstrip()
    report.insert_one({'reportTime': now,'reportTotal':total,'reportResult':result}) # 結果總表
    hook = 'https://hooks.slack.com/services/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'
    requests.post(hook, json={'text': str({'reportTime': now,'reportTotal':total,'reportResult':result})}, headers={'Content-Type': 'application/json'})
    data = dict()
    for i in res:
        if i.xpath('./@class')==['passClass warning'] or i.xpath('./@class') == ['errorClass warning']:
           test_case = i.xpath('./td[1]//text()').pop()
        if i.xpath('./td[1]/div/@class') != []:
            test_name = i.xpath('./td[1]/div//text()').pop()
            result = reusltProcess(i.xpath('./td[2]/button//text()'))
            description = descriptionProcess(i.xpath('./td[2]/div/div/pre//text()'))
            data['testName']=test_name
            data['Result']=result
            data['description'] = description
            data['testTime']=now
            data = {'testCase':test_case,'testName':test_name,'Result':result,'description':description,'testTime':now}
            col.insert_one(data) #細項報表
            data.clear()
    
        
        
def reusltProcess(text):
    if text == []:
        return 'Pass'
    result=re.sub(r'[\n ]','',text[0])
    if result=='通過':
        return 'True'
    elif result=='失敗':
        return 'False'
    else:
        return 'Error'

def descriptionProcess(text):
    if text == []:
        return ''
    result=re.sub(r'[\n ]','',text[0])
    return result