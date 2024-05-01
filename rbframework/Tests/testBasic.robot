*** Settings ***
Library  SeleniumLibrary
Library  Collections
Resource  ../Lib/siteSelect.robot
Resource  ../Lib/loginRegister.robot
Resource  ../Lib/memberSelect.robot
#Resource  ../Lib/memberCenter.robot
Resource  ../Lib/memberData.robot
Suite Setup  Open Browser      Chrome
Test Setup  LoginProcess
Test Teardown  LogOut    ${langage}

*** Variables ***
${langage}=  "cht"

*** Keywords ***
LoginProcess
  MemberSelect    ${langage}    會員中心
  IF  ${langage} == "en"
    ChangeLanage    ${langage}
  END
  ${loginInfo}=  Create Dictionary  identity="member"  langage=${langage}  value={"phone":"+886999999918","veriftycode":"999999"}
  loginRegister.LoginVerifty   ${loginInfo}

*** Test Cases ***
TestLogin
  [Documentation]  # 登入
  [Tags]  Member
  Element Should Be Visible    //div[contains(@class,"menu__member")]
TestGameList
  [Documentation]  # 遊戲列表
  [Tags]  Game
    IF  ${langage} == "en"
     siteSelect  'Games'
    ELSE
      siteSelect  '遊戲'
    END
    Element Should Be Visible    //div[contains(@class,"game__container")]

TestGameDetail
  [Documentation]  # 遊戲詳細
TestDeposit
  [Documentation]  # 商城
TestDepositBuy
  [Documentation]  # 買禮包
TestSerialCode
  [Documentation]  # 兌換
TestStoreLocal
  [Documentation]  # 門市據點
TestRankList
  [Documentation]  # 排行榜
TestTwitter
  [Documentation]  # 推特
TestChatRoom
  [Documentation]  # 聊天室
TestTransferWallet
  [Documentation]  # 轉帳
TestMemberCenter
  [Documentation]  # 會員中心
TestMemberCenterGift
  [Documentation]  # 贈禮打包
TestMemberCenterIconFrame
  [Documentation]  #頭像匡
TestMemberData
  [Documentation]  # 會員資料
TestMemberDataNickName
  [Documentation]  # 改暱稱
TestMemberDataCopyInvitationCode
  [Documentation]  # 分享邀請碼
TestOrderList
  [Documentation]  # 訂單列表
TestOrderListGiftSendRecord
  [Documentation]  # 贈禮紀錄
TestOrderListGiftReceiveRecord
  [Documentation]  # 收禮紀錄

