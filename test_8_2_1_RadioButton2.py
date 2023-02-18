# Check Box
#заходим на сайт разворачиваем меню Home(т.е. родитель) и видим три потомка(папки)
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://testpages.herokuapp.com/styled/basic-html-form-test.html')
driver.maximize_window()

time.sleep(10)

radiobutton_1 = driver.find_element(By.XPATH, "//input[@value='rd1']")#RadioButton1отмечаем
radiobutton_1.click()
print("Click RadioButton_1")
time.sleep(5)

radiobutton_2 = driver.find_element(By.XPATH, "//input[@value='rd2']")#RadioButton1отмечаем
radiobutton_2.click()
print("Click RadioButton_2")
time.sleep(5)

radiobutton_3 = driver.find_element(By.XPATH, "//input[@value='rd3']")#RadioButton1отмечаем
radiobutton_3.click()
print("Click RadioButton_3")
