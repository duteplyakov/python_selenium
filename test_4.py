# делаем скроллин страницы вниз на 200 пикселей!
import datetime
import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
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

"""делаем скроллинг страницы X, Y, где Х это горизонталь а Y - вертикаль, цифры это пиксели"""
#driver.execute_script("windows.scrollTo(0, 300)") #вариант первый
driver.execute_script("window.scrollTo(0, window.scrollY + 200)") # опускает страницу по вертикали на 200 пикселей вниз

time.sleep(3)

"""делаем скриншот"""
now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M")#устанавливаем время скриншота
name_screen = "screen" + now_date + '.png'
driver.save_screenshot("./screen_test_qa/" + name_screen)# делаем скриншот страницы


