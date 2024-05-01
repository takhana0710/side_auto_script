import re
import requests
header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'accept': 'application/json, text/plain, */*'
        }
# url = 'https://10minutemail.net/'

# res = requests.get(url,headers=header).text

with open('test.html', 'r', encoding='utf-8') as f:
    res = f.read()
    f.close()
reg = re.compile('value="([0-9A-Za-z]+@[0-9A-Za-z]+.com)"',re.S).findall(res)
print(reg)
