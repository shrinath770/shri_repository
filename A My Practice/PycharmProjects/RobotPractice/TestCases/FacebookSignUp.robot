*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}  https://facebook.com

*** Test Cases ***
Facebook Signup
    Open Facebook
    input text  id=u_0_m  abc
    input text  id=u_0_o  xyz
    input text  id=u_0_r  1234567891
    input text  id=u_0_w  mypassword
    select from list by value   birthday_day    9
    select from list by value   birthday_month  9
    select from list by value   birthday_year   1995
    select radio button     sex     1
    select radio button     sex     2
    click element   xpath=.//*[@id='u_0_13']
    sleep   4
    Go To       ${url}
    input text  id=email    1234567891
    input text  id=pass     mypassword
    click element   xpath://*[@id="loginbutton"]
    sleep   5
    close browser

*** Keywords ***
Open Facebook
    ${options}=    Evaluate  sys.modules['selenium.webdriver.chrome.options'].Options()    sys
    Call Method     ${options}    add_argument    --disable-notifications
    ${driver}=    Create Webdriver    Chrome    options=${options}
    Go To       ${url}
    maximize browser window
    set selenium speed  1