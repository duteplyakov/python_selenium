#Selenium fo Firefox in MacBookM1
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path = '//Users/denis/Desktop/python_selenium/geckodriver')
driver.get('https://www.saucedemo.com')
user_name = driver.find_element(By.ID, "user-name") #определяем(локатор) строку user
user_name.send_keys("standard_user") #вводим логин в строку user

