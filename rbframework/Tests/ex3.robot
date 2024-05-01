*** Settings ***
Documentation  Wikipedoas Conditional Testing
Library  SeleniumLibrary
Library  OperatingSystem
*** Variables ***

*** Test Cases ***
Verify that if you find Wikivoyage on the page, then click on it and validate (Go to If)
  [Documentation]  This test case verifies if we find Wikivoyage on the page, then we click on it.
  [Tags]  Regression
  ${json}=  Get file  Tests/env.json
  Log To Console    ${json}
#  Open Browser      Chrome
##  Wait Until Element Is Visible    //div[contains(@class,"menu__member")]
##  Click Button  //div[contains(@class,"menu__member")]
#  ${count}=  Get Element Count  //ul[contains(@class,"aside__list")]/li[contains(@class,"md:block")]
#  Run Keyword If    ${count} == 1
#  ...    Log To Console  error
#  ...  ELSE IF    ${count} >8
#  ...    Log To Console  error
#  ...  ELSE
#  ...    GPGLogin
#  Close Browser
*** Keywords ***
GPGLogin
  Click Element    //div[contains(@class,"menu__member")]
  Click Element    //span[contains(text(),"會員中心")]
  Input Text    class:vti__input    +  
  Wait Until Element Is Not Visible    //button[contains(@class,"bg-purpleLine")]
  Click Button    //button[contains(@class,"bg-purpleBtn")]
  Wait Until Element Is Visible  //input[contains(@class,"actual__input__box")]
  Input Text    //input[contains(@class,"actual__input__box")]    999999
  Click Button    //button[contains(@class,"bg-purpleBtn")]