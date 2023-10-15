#print("hello")

from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get('https://www.google.com/')

# os.environ['PATH'] += r"C:/SeleniumDrivers" # need??
driver = webdriver.Chrome()
# driver.get("https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html")
driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")
driver.implicitly_wait(30)
my_element = driver.find_element_by_id('downloadButton')
my_element.click()

