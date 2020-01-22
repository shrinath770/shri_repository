*** Settings ***
Library     SeleniumLibrary
Variables   /home/shri/PycharmProjects/RobotPractice/PageObject/Locators.py

*** Keywords ***
Open my browser
    ${options}=    Evaluate  sys.modules['selenium.webdriver.chrome.options'].Options()    sys
    Call Method     ${options}    add_argument    --disable-notifications
    ${driver}=    Create Webdriver    Chrome    options=${options}
    [arguments]     ${SiteUrl}  ${Browser}
    Go to    ${SiteUrl}
    maximize browser window

Enter username
    [arguments]  ${username}
    input text  ${txt_loginUsername}    ${username}

Enter password
    [arguments]  ${password}
    input text  ${txt_loginPassword}    ${password}

Click LogIn
    click element   ${btn_SignIn}

Verify succesfull login
    title should be     Facebook

close my browser
    Close All Browsers
