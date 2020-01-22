from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser=webdriver.Firefox(executable_path='./geckodriver')
browser.set_window_size(1000,1000)
browser.set_window_position(0,0)
sleep(1)

browser.get("https://www.google.com/")
browser.find_element_by_name("q").send_keys("Chhatrapati")
browser.find_element_by_name("q").send_keys(Keys.RETURN)

sleep(15)
browser.close()
