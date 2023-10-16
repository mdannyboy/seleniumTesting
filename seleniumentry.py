#print("hello")

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get('https://www.google.com/')

# os.environ['PATH'] += r"C:/SeleniumDrivers" # need??
driver = webdriver.Chrome()
# driver.get("https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html")
driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")
driver.implicitly_wait(30)
# my_element = driver.find_element_by_name('downloadButton')
my_element = driver.find_element(By.ID, 'downloadButton')
time.sleep(2)
my_element.click()
time.sleep(5)
