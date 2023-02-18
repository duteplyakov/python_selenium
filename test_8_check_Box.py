# Check Box
#заходим на сайт разворачиваем меню Home(т.е. родитель) и видим три потомка(папки)
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://demoqa.com/checkbox')
driver.maximize_window()


check_box = driver.find_element(By.XPATH, "//button[@aria-label='Toggle']")#Home
check_box.click()#кликаем на > для раскрытия меню
time.sleep(3)
check_box_desktop = driver.find_element(By.XPATH, "//label[@for='tree-node-desktop']")#desktop
check_box_desktop.click()
check_box_documents = driver.find_element(By.XPATH, "//label[@for='tree-node-documents']")#document
check_box_documents.click()
check_box_downloads = driver.find_element(By.XPATH, "//label[@for='tree-node-downloads']")#download
check_box_downloads.click()
