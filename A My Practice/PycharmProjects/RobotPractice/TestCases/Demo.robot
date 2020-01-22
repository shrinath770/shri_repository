*** Settings ***
Library     SeleniumLibrary
Resource    /home/shri/PycharmProjects/RobotPractice/Resources/Loginkeywords.robot

*** Variables ***
${Browser}  crome
${SiteUrl}  https://www.facebook.com/
${user}     shrinath.hattekar@gmail.com
${pwd}  Aditi@143

*** Test Cases ***
Demo
    set selenium speed  2
    Open my browser  ${SiteUrl}  ${Browser}
    Enter username  ${user}
    Enter password  ${pwd}
    Click LogIn
    Verify succesfull login
    close my browser