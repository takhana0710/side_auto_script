import time
import unittest
from testcase.gpg2_chromeset import ma_api, BackAPI
import logging
import inspect
import filetype
class Test_PresentCombination_api(unittest.TestCase):
    """商品組合"""
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_01_GPG_PackageItemGet(self):
        """測試總代理取得贈品列表是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',payload={'IsEnable':1}, api_url=BackAPI.voucher_packageItemGet.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_02_GPG_PackageGet(self):
        """測試總代理取得產品組合列表是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',
                             payload={'Skip': 0,'Show': 50,'Field': 'PackageName',
                                      'OrderType': 'desc','IsEnable': 1,
                                      'IsFuzzySearch': True},
                             api_url=BackAPI.voucher_packageGet.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_03_GPG_PackageAdd(self):
        """測試總代理新增產品組合是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',payload={'IsEnable':1}, api_url=BackAPI.voucher_packageItemGet.value)['Data'].pop()
        data ={
            'PackageName':'  ',
            'PayAmount':'  ',
            'Description':'   test',
            'Specification':'   test',
            'Items[0].ItemQuantity':5
        }
        for k,v in res.items():
            data[f'Items[0].{k}']=v
        files = [
            ('Photo',('autoTest.jpg', open('../autoTest.jpg','rb'), filetype.guess('../autoTest.jpg').mime)),
            ('Photo',('autoT.jpg', open('../1280.jpeg','rb'), filetype.guess('../1280.jpeg').mime)),
        ]
        res = api.uploadFile(api_url=BackAPI.voucher_packageAdd.value,data=data,file=files)
        self.assertEqual('Success', res['Status']['Message'])

    def test_04_GPG_PackageEdit(self): # 改讀 get 資料塞 value 回去
        """測試總代理編輯產品組合是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res=api.apiGetData(method='get',payload={'Skip': 0,'Show': 50,'Field': 'PackageName',
                                                 'OrderType': 'desc','PackageName': '  ',
                                                 'IsEnable': 1,'IsFuzzySearch': True},
                           api_url=BackAPI.voucher_packageGet.value)['Data'].pop()
        del res['Photos']
        res['Description']=str(time.time())
        res = api.uploadFile(data=res,api_url=BackAPI.voucher_packageEdit.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_05_GPG_PackagePhotoDel(self):
        """測試總代理刪除產品組合照片是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res=api.apiGetData(method='get',payload={'Skip': 0,'Show': 50,'Field': 'PackageName',
                                                 'OrderType': 'desc','PackageName': '  ',
                                                 'IsEnable': 1,'IsFuzzySearch': True},
                           api_url=BackAPI.voucher_packageGet.value)['Data'].pop()
        res = api.apiGetData(method='post', api_url=BackAPI.voucher_packagePhotoDel.value,
                             data={'PackageID': res['PackageID'],'PackagePhotoID':res['Photos'][0]['PackagePhotoID']})
        self.assertEqual('Success', res['Status']['Message'])

    def test_06_GPG_PackageDel(self):
        """測試總代理刪除產品組合是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res=api.apiGetData(method='get',payload={'Skip': 0,'Show': 50,'Field': 'PackageName',
                                                 'OrderType': 'desc','PackageName': '  ',
                                                 'IsEnable': 1,'IsFuzzySearch': True},
                           api_url=BackAPI.voucher_packageGet.value)['Data'].pop()
        res = api.apiGetData(method='post', api_url=BackAPI.voucher_packageDel.value,
                             data={'PackageID': res['PackageID']})
        self.assertEqual('Success', res['Status']['Message'])

    def test_A_agent_PackageItemGet(self):
        """測試A代理取得贈品列表是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',payload={'IsEnable':1}, api_url=BackAPI.voucher_packageItemGet.value)
        self.assertEqual('', res)

    def test_B_agent_PackageItemGet(self):
        """測試B代理取得贈品列表是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',payload={'IsEnable':1}, api_url=BackAPI.voucher_packageItemGet.value)
        self.assertEqual('', res)

    def test_C_agent_PackageItemGet(self):
        """測試C代理取得贈品列表是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',payload={'IsEnable':1}, api_url=BackAPI.voucher_packageItemGet.value)
        self.assertEqual('', res)

    def test_A_agent_PackageGet(self):
        """測試A代理取得贈品列表是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'Skip': 0,'Show': 50,'Field': 'PackageName',
                                      'OrderType': 'desc','IsEnable': 1,
                                      'IsFuzzySearch': True},
                             api_url=BackAPI.voucher_packageGet.value)
        self.assertEqual('', res)

    def test_B_agent_PackageGet(self):
        """測試B代理取得贈品列表是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'Skip': 0,'Show': 50,'Field': 'PackageName',
                                      'OrderType': 'desc','IsEnable': 1,
                                      'IsFuzzySearch': True},
                             api_url=BackAPI.voucher_packageGet.value)
        self.assertEqual('', res)

    def test_C_agent_PackageGet(self):
        """測試C代理取得贈品列表是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get',
                             payload={'Skip': 0,'Show': 50,'Field': 'PackageName',
                                      'OrderType': 'desc','IsEnable': 1,
                                      'IsFuzzySearch': True},
                             api_url=BackAPI.voucher_packageGet.value)
        self.assertEqual('', res)

    def test_A_agent_PackageAdd(self):
        """測試A代理新增產品組合是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        data ={
            'PackageName':'  ',
            'PayAmount':'  ',
            'Description':'   test',
            'Specification':'   test',
            'Items[0].ItemQuantity':5
        }
        files = [
            ('Photo',('autoTest.jpg', open('../autoTest.jpg','rb'), filetype.guess('../autoTest.jpg').mime)),
            ('Photo',('autoT.jpg', open('../1280.jpeg','rb'), filetype.guess('../1280.jpeg').mime)),
        ]
        res = api.uploadFile(api_url=BackAPI.voucher_packageAdd.value,data=data,file=files)
        self.assertEqual('', res)

    def test_A_agent_PackageEdit(self): # 改讀 get 資料塞 value 回去
        """測試A代理編輯產品組合是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = dict()
        res['Description']=str(time.time())
        res = api.uploadFile(data=res,api_url=BackAPI.voucher_packageEdit.value)
        self.assertEqual('Success', res)

    def test_A_agent_PackagePhotoDel(self):
        """測試A代理刪除產品組合照片是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post', api_url=BackAPI.voucher_packagePhotoDel.value,
                             data={'PackageID': 100,'PackagePhotoID':1})
        self.assertEqual('', res)

    def test_A_agent_PackageDel(self):
        """測試A代理刪除產品組合是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post', api_url=BackAPI.voucher_packageDel.value,
                             data={'PackageID':1})
        self.assertEqual('', res)

    def test_B_agent_PackageAdd(self):
        """測試B代理新增產品組合是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        data ={
            'PackageName':'  ',
            'PayAmount':'  ',
            'Description':'   test',
            'Specification':'   test',
            'Items[0].ItemQuantity':5
        }
        files = [
            ('Photo',('autoTest.jpg', open('../autoTest.jpg','rb'), filetype.guess('../autoTest.jpg').mime)),
            ('Photo',('autoT.jpg', open('../1280.jpeg','rb'), filetype.guess('../1280.jpeg').mime)),
        ]
        res = api.uploadFile(api_url=BackAPI.voucher_packageAdd.value,data=data,file=files)
        self.assertEqual('', res)

    def test_B_agent_PackageEdit(self): # 改讀 get 資料塞 value 回去
        """測試B代理編輯產品組合是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = dict()
        res['Description']=str(time.time())
        res = api.uploadFile(data=res,api_url=BackAPI.voucher_packageEdit.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_B_agent_PackagePhotoDel(self):
        """測試B代理刪除產品組合照片是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post', api_url=BackAPI.voucher_packagePhotoDel.value,
                             data={'PackageID': 100,'PackagePhotoID':1})
        self.assertEqual('', res)

    def test_B_agent_PackageDel(self):
        """測試B代理刪除產品組合是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post', api_url=BackAPI.voucher_packageDel.value,
                             data={'PackageID':1})
        self.assertEqual('', res)

    def test_C_agent_PackageAdd(self):
        """測試C代理新增產品組合是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        data ={
            'PackageName':'  ',
            'PayAmount':'  ',
            'Description':'   test',
            'Specification':'   test',
            'Items[0].ItemQuantity':5
        }
        files = [
            ('Photo',('autoTest.jpg', open('../autoTest.jpg','rb'), filetype.guess('../autoTest.jpg').mime)),
            ('Photo',('autoT.jpg', open('../1280.jpeg','rb'), filetype.guess('../1280.jpeg').mime)),
        ]
        res = api.uploadFile(api_url=BackAPI.voucher_packageAdd.value,data=data,file=files)
        self.assertEqual('', res)

    def test_C_agent_PackageEdit(self): # 改讀 get 資料塞 value 回去
        """測試C代理編輯產品組合是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = dict()
        res['Description']=str(time.time())
        res = api.uploadFile(data=res,api_url=BackAPI.voucher_packageEdit.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_C_agent_PackagePhotoDel(self):
        """測試C代理刪除產品組合照片是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post', api_url=BackAPI.voucher_packagePhotoDel.value,
                             data={'PackageID': 100,'PackagePhotoID':1})
        self.assertEqual('', res)

    def test_C_agent_PackageDel(self):
        """測試C代理刪除產品組合是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post', api_url=BackAPI.voucher_packageDel.value,
                             data={'PackageID':1})
        self.assertEqual('', res)