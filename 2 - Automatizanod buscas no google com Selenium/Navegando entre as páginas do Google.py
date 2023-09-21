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
numero_resultados = int(resultados.split('Aproximadamente ')[1].split('resultados')[0].replace('.',''))
maximo_paginas = numero_resultados/10
print("Numero de paginas: %s" % (maximo_paginas))

url_pagina =driver.find_element(By.XPATH, '//*[@id="botstuff"]/div/div[3]/div[4]/a[1]/h3/div/span[2]')

pagina_atual = 0
start = 10
while pagina_atual <= 10:
    if not pagina_atual == 0:
        url = url_pagina.replace("start = %s" % start, "start=%s" % (start+10))
        start += 10
    pagina_atual += 1
    driver.get(url_pagina)
