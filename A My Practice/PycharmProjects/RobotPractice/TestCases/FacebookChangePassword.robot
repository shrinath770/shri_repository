*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}  https://facebook.com

*** Test Cases ***
ChangePassword
    Facebook Login
    #sleep   4
    click element   xpath://*[@id='userNavigationLabel']
    #sleep    2s
    click element   xpath://span[text()='Settings']
    click element   xpath://*[@id="navItem_security"]
    click element   xpath:.//*[@class='_51mx']//child::td[@class='_51m- hLeft']//child::span[text()='Change password']
    input text  id=password_old     pass
    input text  id=password_new     pass
    input text  id=password_confirm     pass
    click element   xpath:.//*[@class='submit uiButton uiButtonConfirm']
    close browser

*** Keywords ***
Facebook Login
    ${options}=    Evaluate  sys.modules['selenium.webdriver.chrome.options'].Options()    sys
    Call Method     ${options}    add_argument    --disable-notifications
    ${driver}=    Create Webdriver    Chrome    options=${options}
    Go To       ${url}
    maximize browser window
    set selenium speed  2
    input text  id=email    userid
    input text  id=pass     password
    #sleep   2
    click element   xpath://*[@id="loginbutton"]