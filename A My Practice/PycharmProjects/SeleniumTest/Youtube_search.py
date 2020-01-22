from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
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
driver.set_window_size(1300,800)


driver.get("https://www.youtube.com/")
driver.find_element_by_xpath('.//input[@id="search"]').send_keys("Automation Testing")
sleep(2)
driver.find_element_by_xpath('.//*[@id="search-icon-legacy"]').click()
sleep(2)
driver.find_element_by_xpath('.//a[contains(text(),"Selenium Tutorial For Beginners")]').click()
sleep(2)
driver.quit()