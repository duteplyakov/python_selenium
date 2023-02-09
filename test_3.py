# вводим логин и с помощью кода удаляем один символ!
import time

from selenium import webdriver
from selenium.webdriver import Keys
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

#password = driver.find_element(By.XPATH, '//input[@id="password"]')
#password.send_keys(password_all)
#print("Input Password")

#button_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
#button_login.click()
#print("Click Login Button")
time.sleep(5)
user_name.send_keys(Keys.BACKSPACE) #импортируем KEYS и добавляем BACKSPACE он стирает последний символ ввода логина
user_name.send_keys("r") # возвращаем удаленный символ "r"
















