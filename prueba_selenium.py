import time
from sys import executable
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.cl/")

elemento_web = driver.find_element(By.NAME, 'q')
elemento_web.send_keys("Selenium Automatización 2025" + Keys.ENTER)


time.sleep(30)

