*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}  http://10.129.12.79/

*** Test Cases ***
DI SignIn
    Open DI
    input text  name=formControlTenant   SevOne
    input text  name=formControlName    admin
    input text  name=formControlPassword   SevOne
    click element   xpath=//*[@id="themed-scope-root"]/div[3]/div[1]/div/form/div[4]/div/label/div
    click element   xpath=//*[text()="Login"]
    sleep   6
    click element   xpath=//*[text()="Reports Shared with Me"]
#    input text   xpath=//*[@placeholder="Page"]     2
    close browser

*** Keywords ***
Open DI
    ${options}=    Evaluate  sys.modules['selenium.webdriver.chrome.options'].Options()    sys
    Call Method     ${options}    add_argument    --disable-notifications
    ${driver}=    Create Webdriver    Chrome    options=${options}
    Go To       ${url}
    maximize browser window
    set selenium speed  1