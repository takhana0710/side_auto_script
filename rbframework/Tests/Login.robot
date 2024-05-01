*** Settings ***
Documentation  Login Functionality
Library  SeleniumLibrary
*** Variables ***

*** Test Cases ***
Verify Success Login to GPG
  [Documentation]  This test case verifiles that user is able to successfully Login to GPG
  [Tags]  Login
  Open Browser      Chrome
  Wait Until Element Is Visible  //div[contains(@class,"menu__member")]  timeout=5
  Click Element    //div[contains(@class,"menu__member")]
  Click Element    //span[contains(text(),"會員心")]
  Input Text    class:vti__input      
  Wait Until Element Is Not Visible    //button[contains(@class,"bg-purpleLine")]
  Click Button    //button[contains(@class,"bg-purpleBtn")]
  Wait Until Element Is Visible  //input[contains(@class,"actual__input__box")]
  Input Text    //input[contains(@class,"actual__input__box")]    999999
  Click Button    //button[contains(@class,"bg-purpleBtn")]
  Close Browser


*** Keyword ***