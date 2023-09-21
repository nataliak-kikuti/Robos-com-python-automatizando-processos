import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

print('Iniciando nosso robô... \n')

driver = webdriver.Chrome()

driver.get("https://registro.br/")
dominios = ["roboscompython.com.br", "udemy.com", "uol.com.br", "pythoncurso.com"]

for dominio in dominios:
    pesquisa = driver.find_element(By.ID, 'is-avail-field')
    pesquisa.clear()
    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(2)
    resultados = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/section/div[2]/div/p/span/strong').text
    print("Domínio %s %s" % (dominio, resultados))

driver.close()
