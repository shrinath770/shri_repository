from selenium import webdriver
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
driver.set_window_size(1200, 800)
driver.set_window_position(0, 0)

driver.get("https://www.facebook.com/")
sleep(3)
driver.find_element(By.XPATH, './/*[text()="Sign Up"]').click()
sleep(3)
driver.find_element(By.XPATH, ".//*[@name='firstname']").send_keys("selenium")
driver.find_element(By.XPATH, ".//*[@name='lastname']").send_keys("automation")
sleep(3)
driver.find_element(By.XPATH, ".//*[@name='reg_email__']").send_keys("abc@gmail.com")
sleep(3)
driver.find_element(By.XPATH, ".//*[@name='reg_email_confirmation__']").send_keys("abc@gmail.com")
sleep(3)
driver.find_element(By.XPATH, ".//*[@name='reg_passwd__']").send_keys("mypass")

driver.find_element(By.XPATH, ".//*[@name='birthday_day']").send_keys("12")
sleep(2)
driver.find_element(By.XPATH, ".//*[@name='birthday_month']").send_keys("Sept")
sleep(2)
driver.find_element(By.XPATH, ".//*[@name='birthday_year']").send_keys("1995")
sleep(3)

driver.find_element_by_id("u_0_7").click()
driver.find_element(By.XPATH, ".//*[@name='websubmit']").click()
sleep(25)
driver.quit()