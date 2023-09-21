import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

pesquisa =  input("Digite a pesquisa: ")

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

campo = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
campo.send_keys(pesquisa)
campo.send_keys(Keys.ENTER)

resultados = driver.find_element(By. ID, 'result-stats').text
print(resultados)


time.sleep(5)
driver.quit()

