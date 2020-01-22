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

driver.get("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
ele=driver.find_element_by_xpath('//input[@type="email"]').send_keys('userid')
driver.find_element_by_xpath('//span[@class="RveJvd snByac"]').click()
sleep(2)
driver.find_element_by_xpath('//input[@type="password"]').send_keys('password')
driver.find_element_by_xpath('//span[@class="RveJvd snByac"]').click()
sleep(4)
driver.find_element_by_xpath('.//a[@class="gb_D gb_Oa gb_i"]').click()
sleep(4)
driver.find_element_by_xpath('.//a[@class="gb_Fb gb_5f gb_dg gb_Ne gb_Vc"]').click()
sleep(2)
driver.find_element_by_xpath('.//div[contains(text(),"Remove an account")]').click()
sleep(2)
driver.find_element_by_xpath('.//*[@class="n3x5Fb"]').click()
sleep(2)
driver.find_element_by_xpath('.//div[@class="U26fgb O0WRkf oG5Srb C0oVfc kHssdc M9Bg4d"]').click()
sleep(2)
driver.quit()