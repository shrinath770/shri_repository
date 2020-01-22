from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})

driver = webdriver.Chrome(chrome_options=option,executable_path='/home/shri/PycharmProjects/SeleniumTest/chromedriver')
driver.set_window_size(1200, 700)
driver.set_window_position(0, 0)
sleep(1)

driver.get("http://en-gb.facebook.com/login/")
driver.find_element_by_id("email").send_keys("username")
driver.find_element_by_id("pass").send_keys("password")
driver.find_element_by_id("loginbutton").send_keys(Keys.RETURN)
sleep(4)

driver.find_element(By.XPATH, './/*[@id="userNavigationLabel"]').click()
sleep(4)
driver.find_element(By.XPATH, './/*[text()="Log Out"]').click()

sleep(4)
driver.quit()
