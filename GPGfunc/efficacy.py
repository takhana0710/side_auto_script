import numpy as np
import pymongo
from testcase.gpg2_chromeset import driver_eng
import time
client = pymongo.MongoClient('127.0.0.1', 27017)

def page():
    driver = driver_eng(url='')
    time.sleep(5)
    return driver.per_time,driver.per_getEntries
def collect():
    for _ in range(10):
        per_time,per_genEntries=page()
        # print(per_time)
        db = client['efficacy']
        col = db['index_2']
        for i in per_genEntries:
            # print(i)
            try:
                col.insert_one(i)
            except:
                for k,v in i.items():
                    if type(v)==int:
                        print(k, v)
                        i.update({k:str(v)})
                print(i)
                col.insert_one(i)
        # col.insert_many(per_genEntries)
        dblist = client.list_database_names()

collect()
        
#
# db = client['efficacy']
# col = db['index_2']
# app_result = col.aggregate([{
#     "$group":{
#         "_id":"$name",
#         "duration":{"$avg":"$duration"}
#     }}])
# li = list(app_result)
# print(li)
# print(len(li))
# sort_res = sorted(li,key=lambda x:x['duration'],reverse=True)
# for i in sort_res:
#     print(i)