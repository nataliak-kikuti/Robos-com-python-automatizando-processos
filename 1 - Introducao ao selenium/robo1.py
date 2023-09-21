import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

print('Iniciando nosso robo... \n')

driver = webdriver.Chrome()

driver.get("https://registro.br/")

pesquisa = driver.find_element(By.ID, 'is-avail-field')
pesquisa.clear()
dominio = "roboscompython.com.br"
pesquisa.send_keys(dominio)

pesquisa.send_keys(Keys.RETURN)
time.sleep(2)

resultados = driver.find_element(By. XPATH, '//*[@id="app"]/div/main/div/section/div[2]/div/p/span/strong').text
print("Dominio %s %s" % (dominio, resultados))

time.sleep(3)
driver.close()