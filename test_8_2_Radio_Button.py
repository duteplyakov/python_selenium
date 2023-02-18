# Radio Button - выбо только одно из предложенных элементов

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://demoqa.com/radio-button')
driver.maximize_window()


radio_button = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
radio_button.click()
time.sleep(3)
print("ok")

radio_button = driver.find_element(By.XPATH, "//label[@for='impressiveRadio']")
radio_button.click()
time.sleep(3)
print("ok")

#проверяем после нажатия Impressive, появляется надпись You have selected Impressive вот
# и сверяем что надпись появилась и равна кнопки :) Impressive == You have selected Impressive
impressive1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/p/span')
impressive1 = impressive1.text

impressive2 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/label')
impressive2 = impressive2.text
assert impressive1 == impressive2
print("GOOD!!!")
