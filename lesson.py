#Selenium fo Chrome in MacBookM1
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.saucedemo.com')
driver.maximize_window()

#user_name = driver.find_element(By.ID, "user-name") #обращаеммся к строке user по ID вариант-1
#user_name = driver.find_element(By.NAME, "user-name") #обращаеммся к строке user по NAME вариант -2
#user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]') #обращаеммся к строке user по Full XPATH вариант -3
user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]') #обращаемся через input XPATH - вариант - 4
user_name.send_keys("standard_user") #вводим логин в строку user

password = driver.find_element(By.CSS_SELECTOR, '#password')#обращаемся через CSS_SELECTOR
password.send_keys("secret_sauce") #вводим password в строку password

button_login = driver.find_element(By.XPATH, '//input[@value="Login"]') # выбираем кнопку LOGIN
button_login.click() #нажимаем кнопку



#time.sleep(10)
#driver.close()

