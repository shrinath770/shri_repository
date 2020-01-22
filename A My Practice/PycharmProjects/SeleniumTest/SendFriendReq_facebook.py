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


driver.get("http://en-gb.facebook.com/login/")

driver.find_element_by_id("email").send_keys("username")
driver.find_element_by_id("pass").send_keys("password")
driver.find_element_by_id("loginbutton").send_keys(Keys.RETURN)

driver.find_element_by_class_name('_1frb').send_keys("Jeevan Pawar")
sleep(2)
driver.find_element(By.XPATH, './/*[@class="_585_"]').click()

sleep(5)
driver.find_element_by_xpath("//*[contains(text(),'Vritti Solutions Limited')]//ancestor::div[@class='_6v-_']//following-sibling::div[@class='_6v_2']//*[@class='FriendButton']//*[@type='button']").click()
