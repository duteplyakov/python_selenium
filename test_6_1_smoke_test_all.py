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
password.send_keys(password_all) #вводим пароль
print("Input Password")

button_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
button_login.click() #жмем на кнопку логин
print("Click Login Button")

"""INFO Product #1"""
product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]') #находим/определяем товар
value_product_1 = product_1.text
print(value_product_1)

#находим и определяем цену товара
price_product_1 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
select_product_1.click() #жмем на кнопку добавить в корзину
print("Select Product 1")

#второй товар
product_2 = driver.find_element(By.XPATH, '//a[@id="item_0_title_link"]') #находим/определяем товар
value_product_2 = product_2.text
print(value_product_1)

#находим и определяем цену товара
price_product_2 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div')
value_price_product_2 = price_product_2.text
print(value_price_product_2)

select_product_2 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]')
select_product_2.click() #жмем на кнопку добавить в корзину
print("Select Product 2")

cart = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
cart.click() #кликаем на кнопку перейти в корзину
print("Enter Cart")

"""INFO Cart Product 1"""
cart_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')#находим название товара в корзине
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1 #сравниваем название товара на витрине и в корзине
print("INFO Cart Product 1 GOOD! ")

"""INFO Cart Product 2"""
cart_product_2 = driver.find_element(By.XPATH, '//a[@id="item_0_title_link"]')#находим название товара в корзине
value_cart_product_2 = cart_product_2.text
print(value_cart_product_2)
assert value_product_2 == value_cart_product_2 #сравниваем название товара на витрине и в корзине
print("INFO Cart Product 2 GOOD! ")

button_checkout = driver.find_element(By.XPATH, '//button[@id="checkout"]')#жмем на кнопку оплатить(Checkout)
button_checkout.click()
print("Click Checkout")

"""Select User INFO"""

first_name = driver.find_element(By.XPATH, '//input[@id="first-name"]')#находим локатором имя
first_name.send_keys("Denis") #вводим имя
print("Input First Name")

last_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')#находим локатором Фамилию
last_name.send_keys("Teplyakov")#вводим Фамилию в поле
print("Input Last Name")

zip = driver.find_element(By.XPATH, '//input[@id="postal-code"]')#находим поле для ввода индекс почтовый
zip.send_keys("121121")#вводим индекс почтовый
print("Input ZIP")

button_continue = driver.find_element(By.XPATH, '//*[@id="continue"]')
button_continue.click()#кликаем на кнопку Далее
print("Click Button Continue")

"""INFO Finish Product 1"""
#сверяем название продукта и цену с витриной и итоговым
finish_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print("INFO Finish Product 1 GOOD! ")

price_finish_product_1 = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_finish_price_product_1 = price_finish_product_1.text
print(value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1
print("INFO Finish Price Product 1 GOOD! ")


"""INFO Finish Product 2"""
finish_product_2 = driver.find_element(By.XPATH, '//a[@id="item_0_title_link"]')
value_finish_product_2 = finish_product_2.text
print(value_finish_product_2)
assert value_product_2 == value_finish_product_2
print("INFO Finish Product 2 GOOD! ")

price_finish_product_2 = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
value_finish_price_product_2 = price_finish_product_2.text
print(value_finish_price_product_2)
assert value_price_product_2 == value_finish_price_product_2
print("INFO Finish Price Product 2 GOOD! ")


#сверяем Item total сумму и проверяем её с суммой итоговой для оплаты (без тах)
summary_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[5]')
value_summary_price  = summary_price.text
print(value_summary_price)
print("!!!")
#####################

summary_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[5]')
value_summary_price  = summary_price.text
print(value_summary_price)
item1 = value_finish_price_product_1.replace('$', '')
item2 = value_finish_price_product_2.replace('$', '')
total_summ = float(item1) + float(item2)
print(total_summ)
item3 = value_summary_price.replace('$', '')
item4 = item3.replace('Item total:', '')
item5 = float(item4)
print(item5)

assert item5 == total_summ
print("Total summary price GOOD!!!")

