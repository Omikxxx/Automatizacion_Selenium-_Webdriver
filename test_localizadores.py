import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest import mark



def test_element_by_class():
    driver = webdriver.Chrome()
    driver.get('https://opencart.abstracta.us/index.php?route=common/home')

    #web_element = driver.find_element(By.CLASS_NAME, "img-responsive")

    #web_element.click()


    time.sleep(1)