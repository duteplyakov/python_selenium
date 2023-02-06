#Selenium fo Safari in MacBookM1
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()

driver.get('https://www.saucedemo.com')
driver.maximize_window()
user_name = driver.find_element(By.ID, "user-name") #определяем(локатор) строку user
user_name.send_keys("standard_user") #вводим логин в строку user
time.sleep(10)