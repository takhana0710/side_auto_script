import time
import requests
import re
from selenium.webdriver.common.by import By
from testcase.gpg2_chromeset import driver_eng

auth={}
gpg_work_id = ''
def WorkList(**kwargs):
    res = requests.get('https://api.trello.com/1/boards/{board}/lists'.format(board=gpg_work_id),params=auth).json()
    res = list(filter(lambda x:x.get('name')==kwargs.get('name'),res)).pop()
    return res

def CardList(**kwargs):
    res = requests.get('https://api.trello.com/1/list/{listid}/cards'.format(listid=kwargs.get('listid')),params=auth).json()
    return res
#

def CardDetail(**kwargs):
    res = requests.get('https://api.trello.com/1/card/{cardid}'.format(cardid=kwargs.get('cardid')),params=auth).json()
    url=re.compile('規格：(https://.*?)\\n',re.M).findall(res['desc'])
    print(url)
    if url != []:
        return url
    else:
        return None

listid=WorkList(name='QA')
card = CardList(listid=listid.get('id'))
time.sleep(1)
res = list(filter(lambda x: CardDetail(cardid=x.get('id'))!=None,card))

for i in res:
    driver = driver_eng(url=re.compile('規格：(https://.*?)\\n',re.M).findall(i['desc']).pop())
    driver.driver.switch_to.frame(driver.driver.find_element(By.XPATH,'//iframe[@id="mainFrame"]'))
    time.sleep(3)
    source = driver.view_source(filename=i['name'])
    driver.exit()