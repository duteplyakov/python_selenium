# Проверяем авторизацию и попадаем на заглавную страницу!

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

#после входа мы видем страницу где слева вверху
# есть PRODUCT название, т.е таким образом мы удостоверимся, что зашли
#по логину и паролю верно и перешил на следующую страницу
#если логин или пароль не верный то в терминале будет ошибка на переход в данный модуль
text_products = driver.find_element(By.XPATH, '//span[@class="title"]')
value_text_products = text_products.text
print((value_text_products))
assert  value_text_products == "PRODUCTS"
print("Всё работает, перешли на страницу!")


