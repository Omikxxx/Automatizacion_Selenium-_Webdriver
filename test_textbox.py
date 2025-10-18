import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest import mark


def test_textbox_intercation():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selectorshub.com/xpath-practice-page/")

    #frame_element = driver.find_element(By.ID, 'da5f0b1')
    #driver.switch_to.frame(frame_element)

    textbox = driver.find_element(By.NAME,'email')
    textbox.send_keys("prueba@elemento.org")
    textbox.clear()
    textbox.send_keys("volviendo@ingcorreo.org")
    valor_actual = textbox.get_attribute('value')
    print("En el primer text dice", valor_actual)

    textbox = driver.find_element(By.NAME, 'Password')
    textbox.send_keys("prueba@elemento.org")
    textbox
    textbox.send_keys("*******")

    textbox = driver.find_element(By.NAME, 'company')
    textbox.send_keys("Pruebas")
    textbox.clear()
    textbox.send_keys("nuevaprueba")

    textbox = driver.find_element(By.NAME, 'mobile number')
    textbox.send_keys("+5975896425")
    textbox.clear()
    textbox.send_keys("6729320302")

    textbox = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[3]/label/input')
    textbox.send_keys("NuevoPais")
    textbox.clear()
    textbox.send_keys("Volviendo Bye...")

    textbox = driver.find_element(By.XPATH, '//*[@id="inp_val"]')
    textbox.send_keys("El Paso Prueba")
    textbox.clear()
    textbox.send_keys("mas pruebas Adios")
    valor_path = textbox.get_attribute('value')
    print("El valor del ultimo Xpath es:",valor_path)

    time.sleep(5)