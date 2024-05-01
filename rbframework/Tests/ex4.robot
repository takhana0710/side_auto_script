*** Settings ***
Library  SeleniumLibrary
Resource  ../Lib/siteSelect.robot
*** Test Cases ***
Swiper-Test
  Open Browser      Chrome
  siteSelect.SwiperSelect    排行榜