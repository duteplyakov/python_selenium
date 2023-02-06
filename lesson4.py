import time
from selenium import webdriver
options = webdriver.ChromeOptions()

binary_yandex_driver_file = 'Yandex' # path to YandexDriver

driver = webdriver.Chrome(binary_yandex_driver_file, options=options)
driver.get('https://www.saucedemo.com')
driver.maximize_window()

#time.sleep(10)
