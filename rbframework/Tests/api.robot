*** Settings ***
Library  RequestsLibrary
*** Variables ***
${url}  https://ma-gpg.ceis.tw/Token/SignIn
*** Test Cases ***
[Documentation] 測試後台API
  &{header }=  Create Dictionary  Content-Type=
  &{data}=  Create Dictionary  Account=GenesisPerfectGame Password=123456
  ${resp}  POST
  Log  ${resp}
