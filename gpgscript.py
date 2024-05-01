from testcase.gpg2_chromeset import ma_api,BackAPI
api = ma_api()
for i in []:
    api.apiGetData(method='post',api_url=BackAPI.member_customerServiceChange.value,data=
    {"MemberID":i,"PointTypeID":1,"Point":"100000","Note":"測試大量用金幣"}
)
