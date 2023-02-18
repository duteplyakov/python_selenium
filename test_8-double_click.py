# заходим на сайт и ждем 2 раза на кнопку и правой кнопкой мыши

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://demoqa.com/buttons')
driver.maximize_window()

#ActionChains классы обычно используются для автоматизации таких взаимодействий,
# как щелчок контекстного меню , действия кнопки мыши, нажатие клавиши и движения мыши.
action = ActionChains(driver)


double = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")#локатор кнопки doubleClick
action.double_click(double).perform() #тут кликаем и метод perform для сохранения результата кликанья :)
print("Click double_1")
time.sleep(3)

right_click = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")#локатор кнопки rightClick
action.context_click(right_click).perform()
print("right_click")
time.sleep(3)


