import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest import mark



def test_elementby_id():
    driver = webdriver.Chrome()
    driver.get("https://opencart.abstracta.us/index.php?route=common/home")

    buscar = driver.find_element(By.XPATH, '//*[@id="search"]/input').send_keys("Prueba Xpath")

   # encontrado =driver.find_elements(By.CLASS_NAME,"dropdown-toggle")
    #print("Cantidad de elementos Clase: ", len(encontrado))
    #encontrado[3].click()

    driver.find_element(By.XPATH, '/html/body/header/div/div/div[2]/div/span/button/i').click()

    time.sleep(9)