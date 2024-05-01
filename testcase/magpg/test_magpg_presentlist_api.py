import time
import unittest
from testcase.gpg2_chromeset import ma_api, BackAPI
import logging
import inspect
import filetype

class Test_PresentList_api(unittest.TestCase):
    """贈品清單"""
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_01_GPG_ItemGet(self):
        """測試總代理的贈品列表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get', api_url=BackAPI.voucher_itemGet.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_02_GPG_ItemTypeGet(self):
        """測試總代理的類別設定列表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get', api_url=BackAPI.voucher_itemTypeGet.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_03_GPG_ItemTypeAdd(self):
        """測試總代理的新增類別是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='post', data={'ItemTypeName': "  "},
                             api_url=BackAPI.voucher_itemTypeAdd.value)
        self.assertEqual('Success', res['Status']['Message'])

    def test_04_GPG_ItemTypeEdit(self):
        """測試總代理的編輯類別是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get', api_url=BackAPI.voucher_itemTypeGet.value)
        data = list(filter(lambda x: x.get('ItemTypeName') == '  ', res['Data'])).pop()
        data['ItemTypeName'] = 'autoEdit'
        del data['Description']
        res = api.apiGetData(method='post', data=data,api_url=BackAPI.voucher_itemTypeEdit.value)
        self.assertEqual('Success', res['Status']['Message'])
    
    def test_05_GPG_ItemSearch(self):
        """測試總代理的搜尋曾品是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get', payload={'ItemTypeID': 2}, api_url=BackAPI.voucher_itemGet.value)
        self.assertEqual('Success', res['Status']['Message'])
    
    def test_06_GPG_ItemAdd(self):
        """測試總代理的新增贈品是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        filename = open('../autoTest.jpg', 'rb')
        filename2 = open('../1280.jpeg', 'rb')
        data = {
            'ItemName': 'QA自動化測試',
            'ItemTypeID': 1,
            'Description': 'QA自動化測試',
            'Amount': None,
            'Specification': 'QA自動化測試'
        }
        files = [
            ('Photo',('autoTest.jpg', filename, 'image/jpeg')), ('Photo',('1280.jpeg', filename2, 'image/jpeg'))
        ]
        res = api.uploadFile(api_url=BackAPI.voucher_itemAdd.value, data=data,file=files)
        filename.close()
        filename2.close()
        self.assertEqual('Success', res['Status']['Message'])

    def test_07_GPG_ItemEdit(self): # 改讀 get 資料塞 value 回去
        """測試總代理的編輯贈品是否正常成功""" # 0718
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get',
                             api_url=BackAPI.voucher_itemGet.value,
                             payload={'ItemName': 'QA自動化測試'})['Data'].pop()# json
        fileUrl = '../autoTest.jpg'
        kind = filetype.guess(fileUrl)
        data=dict()
        itemPhotoID=res['PhotoPathList'][0]['ItemPhotoID']
        filelist = [open(fileUrl, 'rb')]
        del res['ItemDescription']
        del res['PhotoPathList']
        res['Description']=str(time.time())
        files=[]
        for i,j in enumerate(filelist):
            res[f'Photo[{i}].ItemPhotoID'] = itemPhotoID
            files.append((f'Photo[{i}].PhotoFile',(j.name,j,kind.mime)))
        for k,v in res.items():
            data[str(k)] = (None,v) # 結果在下面
        res = api.uploadFile(api_url=BackAPI.voucher_itemEdit.value,data=data,file=files)
        filelist[0].close() # 關閉檔案
        self.assertEqual('Success', res['Status']['Message'])

    def test_08_GPG_PhotoDel(self):
        """測試總代理刪除圖片是否成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get', api_url=BackAPI.voucher_itemGet.value,
                             payload={'ItemName': 'QA自動化測試'})['Data'].pop()
        res = api.apiGetData(method='post', api_url=BackAPI.voucher_itemPhotoDel.value,
                             data={'ItemID': res['ItemID'],'ItemPhotoID':res['PhotoPathList'][0]['ItemPhotoID']})
        self.assertEqual('Success', res['Status']['Message'])

    def test_09_GPG_ItemDel(self):
        """測試總代理的刪除類別是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api()
        res = api.apiGetData(method='get', api_url=BackAPI.voucher_itemGet.value,
                             payload={'ItemName': 'QA自動化測試'})['Data'].pop()
        res = api.apiGetData(method='post', api_url=BackAPI.voucher_itemDel.value, data={'ItemID': res['ItemID']})
        self.assertEqual('Success', res['Status']['Message'])


    def test_A_agent_ItemTypeEdit(self):
        """測試A代理的編輯類別是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post', data={'ItemTypeID': 1, 'ItemTypeName': "罐頭"},
                             api_url=BackAPI.voucher_itemTypeEdit.value)
        self.assertEqual('', res)

    def test_B_agent_ItemTypeEdit(self):
        """測試B代理的編輯類別是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post', data={'ItemTypeID': 1, 'ItemTypeName': "罐頭"},
                             api_url=BackAPI.voucher_itemTypeEdit.value)
        self.assertEqual('', res)

    def test_C_agent_ItemTypeEdit(self):
        """測試C代理的編輯類別是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post', data={'ItemTypeID': 1, 'ItemTypeName': "罐頭"},
                             api_url=BackAPI.voucher_itemTypeEdit.value)
        self.assertEqual('', res)

    def test_A_agent_ItemTypeAdd(self):
        """測試A代理的新增類別是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post', data={'ItemTypeName': "  "},
                             api_url=BackAPI.voucher_itemTypeAdd.value)
        self.assertEqual('', res)

    def test_B_agent_ItemTypeAdd(self):
        """測試B代理的新增類別是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post', data={'ItemTypeName': "  "},
                             api_url=BackAPI.voucher_itemTypeAdd.value)
        self.assertEqual('', res)

    def test_C_agent_ItemTypeAdd(self):
        """測試C代理的新增類別是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post', data={'ItemTypeName': "  "},
                             api_url=BackAPI.voucher_itemTypeAdd.value)
        self.assertEqual('', res)

    def test_A_agent_ItemTypeGet(self):
        """測試A代理的類別設定列表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get', api_url=BackAPI.voucher_itemTypeGet.value)
        self.assertEqual('', res)

    def test_B_agent_ItemTypeGet(self):
        """測試B代理的類別設定列表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get', api_url=BackAPI.voucher_itemTypeGet.value)
        self.assertEqual('', res)

    def test_C_agent_ItemTypeGet(self):
        """測試C代理的類別設定列表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get', api_url=BackAPI.voucher_itemTypeGet.value)
        self.assertEqual('', res)

    def test_A_agent_ItemGet(self):
        """測試A代理的贈品列表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get', api_url=BackAPI.voucher_itemGet.value)
        self.assertEqual('', res)

    def test_B_agent_ItemGet(self):
        """測試B代理的贈品列表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get', api_url=BackAPI.voucher_itemGet.value)
        self.assertEqual('', res)

    def test_C_agent_ItemGet(self):
        """測試C代理的贈品列表是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='get', api_url=BackAPI.voucher_itemGet.value)
        self.assertEqual('', res)

    def test_A_agent_ItemDel(self):
        """測試A代理的刪除贈品是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',data={'ItemID': 100}, api_url=BackAPI.voucher_itemDel.value)
        self.assertEqual('', res)

    def test_B_agent_ItemDel(self):
        """測試B代理的刪除贈品是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',data={'ItemID': 100}, api_url=BackAPI.voucher_itemDel.value)
        self.assertEqual('', res)

    def test_C_agent_ItemDel(self):
        """測試C代理的刪除贈品是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post',data={'ItemID': 100}, api_url=BackAPI.voucher_itemDel.value)
        self.assertEqual('', res)

    def test_A_agent_ItemEdit(self):
        """測試A代理的編輯贈品是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post', api_url=BackAPI.voucher_itemEdit.value,
                       data={'ItemID':100,'ItemName': 'QA測試AAAA@@@','ItemTypeID': 100,
                             'Description': 'QA測試',
                             'Amount': 1,'Specification': 'QA測試5555','MKItemID': 5555})
        self.assertEqual('', res)

    def test_B_agent_ItemEdit(self):
        """測試B代理的編輯贈品是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post', api_url=BackAPI.voucher_itemEdit.value,
                             data={'ItemID': 100, 'ItemName': 'QA測試AAAA@@@', 'ItemTypeID': 100,
                                   'Description': 'QA測試',
                                   'Amount': 1, 'Specification': 'QA測試5555', 'MKItemID': 5555})
        self.assertEqual('', res)

    def test_C_agent_ItemEdit(self):
        """測試C代理的編輯贈品是否正常成功"""
        logging.info(str(inspect.stack()[0][0].f_code.co_name))  # 取得當前執行的method name
        api = ma_api(account='  ', password='  ')
        res = api.apiGetData(method='post', api_url=BackAPI.voucher_itemEdit.value,
                             data={'ItemID': 100, 'ItemName': 'QA測試AAAA@@@', 'ItemTypeID': 100,
                                   'Description': 'QA測試',
                                   'Amount': 1, 'Specification': 'QA測試5555', 'MKItemID': 5555})
        self.assertEqual('', res)