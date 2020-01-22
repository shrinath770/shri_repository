from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser=webdriver.Firefox(executable_path='./geckodriver')
browser.set_window_size(1000,1000)
browser.set_window_position(0,0)
sleep(1)

browser.get("https://en.wikipedia.org/wiki/Main_Page")
browser.find_element_by_id("searchInput").send_keys("Selenium(software)")
sleep(2)

browser.find_element_by_id("searchInput").send_keys(Keys.RETURN)
browser.execute_script("window.scrollTo(0,600);")
sleep(2)
browser.execute_script("window.scrollTo(0,-600);")

sleep(15)
browser.close()
