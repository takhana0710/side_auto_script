import unittest
import os
from testcase import HTMLTestReportCN
import time
import logging
import requests
import re
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M', handlers=[logging.FileHandler('GPGfunc/my.log', 'w', 'utf-8')])
os_path = os.getcwd()
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test_gpg2_*.py', top_level_dir=None)
    return discover
case_path = os.path.join(os_path, 'testcase/gpg')
now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
# 確定生成報告的路徑
filePath = "test_reports/" + now + "-Test_Result.html"
fp = open(filePath, 'wb')
# 設定
setting = {
    "stream": fp,
    "title": 'GPG前台-自動化測試報告',
    # description=None
    "tester": 'CEIS - QA Team'
}
# 生成報告
runner = HTMLTestReportCN.HTMLTestRunner(**setting)

# 運行測試用例
runner.run(all_case())
# 關閉文件，否則會無法生成文件
fp.close()
# Read(file=filePath)
with open(filePath, 'r', encoding='utf-8') as f:
    r = f.read()
    f.close()

res = re.compile('連線嘗試失敗，因為連線對象有一段時間並未正確回應，或是連線建立失敗，因為連線的主機無法回應。',re.S).findall(r)
if len(res) >10:
    hook = 'https://hooks.slack.com/services/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'
    requests.post(hook, json={'text': '測試結果太多timeout 疑似測試站台掛掉 請查看'}, headers={'Content-Type': 'application/json'})
