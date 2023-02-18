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

checkbox_1 = driver.find_element(By.XPATH, "//input[@value='cb1']")#CheckBox_1 ставим галочку
checkbox_1.click()
print("Click CheckBox_1")
time.sleep(5)

checkbox_3 = driver.find_element(By.XPATH, "//input[@value='cb3']")#CheckBox_3 снимаем галочку
checkbox_3.click()
print("Click CheckBox_3")
time.sleep(5)