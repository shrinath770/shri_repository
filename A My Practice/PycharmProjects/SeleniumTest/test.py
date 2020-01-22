import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='/home/shri/PycharmProjects/SeleniumTest/chromedriver')
driver.set_window_size(1200, 700)
driver.set_window_position(0, 0)
driver.get("https://www.unibet.ro/betting#filter/football")

try:
    element_present = EC.presence_of_element_located((By.CLASS_NAME, 'KambiBC-event-result__score-list'))
    WebDriverWait(driver, 4).until(element_present)
except TimeoutException:
    print('Timed out waiting for page to load')

event = driver.find_elements_by_class_name('KambiBC-event-item KambiBC-event-item--type-match')

for items in event:
    link = items.find_element_by_class_name('KambiBC-event-item__link')
    scoruri = items.find_element_by_class_name('KambiBC-event-item__score-container')

    scor1 = scoruri.find_element_by_xpath(".//li[@class='KambiBC-event-result__match']/span[1]")
    scor2 = scoruri.find_element_by_xpath(".//li[@class='KambiBC-event-result__match']/span[2]")

    print(scor1.text)
    print(scor2.text)
    if scor1.text == '0' and scor2.text == '0':

        link.click()
        time.sleep(3)

        PlajePariuri = driver.find_elements_by_xpath("//ul[@class='KambiBC-list-view__column']")
        for items in PlajePariuri:
            NumePlaje = items.find_element_by_xpath("//li/header/h2")
            print(NumePlaje.text)
