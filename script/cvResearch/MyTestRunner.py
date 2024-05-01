import unittest
from unittest import result
from datetime import datetime


class MyTextTestResult(result.TestResult):
    def __init__(self, descriptions):
        super(MyTextTestResult, self).__init__(descriptions)
        self.descriptions = descriptions
        self.js_data = dict()  # 測試結果json

    def getDescription(self, test):
        doc_first_line = test.shortDescription()
        if self.descriptions and doc_first_line:
            return '\n'.join((str(test), doc_first_line))
        else:
            return str(test)

    def startTest(self, test):
        super(MyTextTestResult, self).startTest(test)

    def addSuccess(self, test):
        super(MyTextTestResult, self).addSuccess(test)
        self.js_data['testCase'] = self.getDescription(test) # 案例名稱
        self.js_data['testResult'] = 'pass' # 測試結果
        self.js_data['testTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 執行時間
        self.js_data['errorMsg'] = '' # 錯誤訊息
        self.js_data['qaCheckReason'] = '' # qa排查狀況註解
        print(self.js_data)

    def addError(self, test, err):
        super(MyTextTestResult, self).addSuccess(test)
        self.js_data['testCase'] = self.getDescription(test)
        self.js_data['testResult'] = 'error'
        self.js_data['testTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.js_data['errorMsg'] = err
        self.js_data['qaCheckReason'] = '' # qa排查狀況註解
        print(self.js_data)

    def addFailure(self, test, err):
        super(MyTextTestResult, self).addFailure(test, err)
        self.js_data['testCase'] = self.getDescription(test)
        self.js_data['testResult'] = 'fail'
        self.js_data['testTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.js_data['errorMsg'] = err
        self.js_data['qaCheckReason'] = '' # qa排查狀況註解
        print(self.js_data)


class MyTextTestRunner(unittest.TextTestRunner):
    NewResultClass = MyTextTestResult

    def __init__(self):
        super(MyTextTestRunner, self).__init__()
        self.descriptions = True

    def _makeResult(self):  # 製作結果
        return self.NewResultClass(self.descriptions)

    def run(self, test):
        result = self._makeResult()
        startTestRun = getattr(result, 'startTestRun', None)
        startTestRun()  # 準備
        test(result)  # 執行
        stopTestRun = getattr(result, 'stopTestRun', None)  # 結束
        stopTestRun()
        return result
