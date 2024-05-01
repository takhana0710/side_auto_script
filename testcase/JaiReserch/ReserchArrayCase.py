import enum
import unittest
from enum import Enum







# 生成器
class TestCoroutine:
    def tset(self):
        print("")


# 迭代器
class TestDadie:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


class TestDadie2_ToForUse:
    start: int
    end: int
    iterNum: int

    def __init__(self, _start, _end):
        self.start = _start
        self.end = _end

    def __iter__(self):
        self.iterNum = self.start
        return self

    def __next__(self):
        temp = 0

        if self.iterNum <= self.end:
            temp = self.iterNum
            self.iterNum += 1
            return temp
        else:
            raise StopIteration


# Class 資料結構型態
class constructClass1:
    value: int
    boolean: bool
    string: str

    def __init__(self, _int, _bool, _str):
        self.value = _int
        self.boolean = _bool
        self.string = _str


class enumType(Enum):
    Type1 = "1111",
    Type2 = 2222,
    Type3 = "1231231f",
    Type4 = '11111',
    Type5 = '22312311',
    Type6 = 1231231,
    Type7 = '1111',


class Test_Case(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ListType(self):
        #############list區##############
        myList = ['111', '222', '333', '111']
        print(myList)  # ['111', '222', '333']
        # 最前面首端加入資料
        myList.append('meeee')
        myList.append(11123)
        print(myList)  # ['111', '222', '333', 'meeee', 11123]
        # 插入元素
        myList.insert(3, "我加入index號")
        print(myList)  # ['111', '222', '333', '我加入index號', '111', 'meeee', 11123]
        # 刪除資料(陣列位子)
        del myList[2]
        print(myList)  # ['111', '222', '我加入index號', '111', 'meeee', 11123]
        # 刪除尾端最後一筆資料
        myList.pop()
        print(myList)  # ['111', '222', '我加入index號', '111', 'meeee']
        # 刪除謀一筆資料(資料內容)
        myList.remove('meeee')
        print(myList)  # ['111', '222', '我加入index號', '111']
        ##########list資料處理#########
        # 反轉排序
        myList.reverse()
        print(myList)  # ['111', '我加入index號', '222', '111']
        # 排序
        myList.sort()
        print(myList)  # ['111', '111', '222', '我加入index號']
        # 查詢某筆資料在資料中第一次出現的位子
        print(myList.index("111"))  # 0
        # 查詢某筆資料在資料中重複次數
        print(myList.count("111"))  # 2

    def test_DictType(self):
        ########dict資料型態###############
        myDict = {
            'myVal1': 1,
            'myVal2': 2,
            'myVal3': "3",
            'myVal4': constructClass1(3, False, "me"),
            'myVal5': False,
        }
        # 索取資料
        print(myDict.get('myVal4'))  # <ReserchArrayCase.constructClass1 object at 0x000001DE27751190>
        print(myDict['myVal4'].value)  # 3
        print(myDict['myVal4'].string)  # me
        print(myDict['myVal4'].boolean)  # False
        # 索取全部的Key
        print(myDict.keys())  # dict_keys(['myVal1', 'myVal2', 'myVal3', 'myVal4', 'myVal5'])
        # 索取全部的Value
        print(
            myDict.values())  # dict_values([1, 2, '3', <ReserchArrayCase.constructClass1 object at 0x000001DE27751190>, False])
        # 索取全部的Item(key,value)
        print(
            myDict.items())  # dict_items([('myVal1', 1), ('myVal2', 2), ('myVal3', '3'), ('myVal4', <ReserchArrayCase.constructClass1 object at 0x000001DE27751190>), ('myVal5', False)])
        # 刪除最後尾端的物件
        myDict.popitem()
        print(
            myDict.items())  # dict_items([('myVal1', 1), ('myVal2', 2), ('myVal3', '3'), ('myVal4', <ReserchArrayCase.constructClass1 object at 0x000001DE27751190>)])
        # 刪除全部物件
        myDict.clear()
        print(myDict)  # {}

        ########dict資料型態(利用enum製作資料:資料會變醜，但是可以避免字串問題)###############
        myDict1 = {
            enumType.Type1: "1111",
            enumType.Type2: 2222,
            enumType.Type3: "1231231f",
            enumType.Type4: '11111',
            enumType.Type5: '22312311',
            enumType.Type6: 1231231,
            enumType.Type7: '1111',
        }
        # 索取資料
        print(myDict1.get(enumType.Type2))  # 2222
        # 索取全部的Key
        print(myDict1.keys())
        # 索取全部的Value
        print(myDict1.values())
        # 索取全部的Item(key,value)
        print(myDict1.items())
        # 刪除最後尾端的物件
        myDict1.popitem()
        print(myDict1.items())
        # 刪除全部物件
        myDict1.clear()
        print(myDict1)

        ###############################################################
        # 長度查詢
        print(len(myDict))
        myDict.clear()
        # 奇怪的轉換
        # print(set(list(myDict1.get(enumType.Type4))))
        # print(list(myDict1.get(enumType.Type4)))
        # print(myDict1)

    def test_DadieType(self):
        # 迭代測試
        # 單一迭
        # myclass = TestDadie()
        # myiter = iter(myclass)
        # print(next(myiter))
        # print(next(myiter))
        # print(next(myiter))
        # print(next(myiter))
        # for迭代 #0.17左右
        # forDadieClass = TestDadie2_ToForUse(0, 1000)
        # forIter = iter(forDadieClass)
        # for index in forIter:
        #     print(index)
        # 一班for循環 #0.158左右
        for index in range(0, 1001):
            print(index)

    def test_CoroutineType(self):
        print("")
