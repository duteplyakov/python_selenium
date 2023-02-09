# вводим логин и пароль  с помощью Enter и делаем сортировку страницы!
# и делаем СКРИНШОТ страницы
import datetime
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

password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
print("Input Password")
password.send_keys(Keys.RETURN) # !!! Данная команда аналог ENTER, мы не пишем код нажатия кнопки!!!!

filter = driver.find_element(By.XPATH, "//select[@data-test='product_sort_container']") # справа в верхнем углу есть фильтр-сортировка, нажимаем на нее
filter.click() #кликаем на сортировку
print("Click Filter")
#time.sleep(3) #задержка по времени чтоб увидеть процесс
#filter.send_keys(Keys.PAGE_DOWN) #иммитируем нажатие кнопки вниз на клавиаторе при сортировке
#time.sleep(3)
#filter.send_keys(Keys.RETURN) #после выпора вниз кликаем иммитация Enter

filtr = driver.find_element(By.XPATH, "//option[@value='lohi']") #второй вариант сортировки
filtr.click()
time.sleep(3)

"""  делаем скриншот страницы """
now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M")#устанавливаем время скриншота
name_screen = "screen" + now_date + '.png'
driver.save_screenshot("./screen_test_qa/" + name_screen)# делаем скриншот страницы






