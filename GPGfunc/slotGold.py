import json
from testcase.gpg2_chromeset import driver_eng, gpg_api
import time
driver = driver_eng(url='  ')
driver.guest()
token, refresh = eval(driver.driver.execute_script('return localStorage.getItem("userToken")'))
print(token, '\t', refresh)
driver2 = driver_eng(url='  ')
token = '\"' + token + '\"'
refresh = '\"' + refresh + '\"'
js = """localStorage.setItem("userToken",\'[{token},{refresh}]\')""".format(token=token, refresh=refresh)
print(js)
driver2.driver.execute_script(js)
driver2.driver.execute_script("location.reload(true);")
time.sleep(100)
