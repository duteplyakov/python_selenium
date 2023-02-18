# На открытой странице после авторизации открываем меню слева раскрывающеся, выбираем
# и нажимаем на About, потом делаем шаг назад в браузере и нажимаем на крестик закрывая меню.
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
base_url = 'https://www.saucedemo.com'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standard_user) #тут ссылаемся на переменную , тк логины разные и в переменной можем менять
print("Input Login") # вывод на экран, что мы делаем, "вводим логин", чисто информативно

password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
print("Input Password")

button_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
button_login.click()
print("Click Login Button")

menu = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]') #кликаем на кнопку меню слева всплываеющее
menu.click()
print("Click Menu Button")
time.sleep(3)
link_about = driver.find_element(By.XPATH, '//a[@id="about_sidebar_link"]') #из всплывающего меню выбираем About и кликаем на него
link_about.click()
time.sleep(3)
print("Click Link About")

#cooki = driver.find_element(By.XPATH, '//*[@id="onetrust-button-group"]') #закрываем открытое cooki
#cooki.click()

driver.back()#возвращаемся на один шаг в браузере назад
menu = driver.find_element(By.XPATH, '//button[@id="react-burger-cross-btn"]') #закрываем открытое меню, жмем на крестик
menu.click()
print("Click Menu Button")
driver.forward()#делаем шаг вперед в браузере

