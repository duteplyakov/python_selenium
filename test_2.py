# Негативное тестирование! Проверяем авторизацию с неправильным логином и паролем!

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
base_url = 'https://www.saucedemo.com'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_use" #ошибочный логин
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

warring_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warring_text = warring_text.text
assert value_warring_text == "Epic sadface: Username and password do not match any user in this service"
print("Test OK!")

#driver.refresh() # строка для обновления страницы