*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}  https://www.youtube.com/

*** Test Cases ***
Youtube Search
    Open Browser  ${url}  chrome
    maximize browser window
    set selenium speed  2s
    input text  name=search_query    Dance like Hardy Sandhu
    click element   xpath://*[@id="search-icon-legacy"]/yt-icon
    click element   xpath://*[@id="video-title"]//following::span[text()="37M views"]
    close browser


*** Keywords ***