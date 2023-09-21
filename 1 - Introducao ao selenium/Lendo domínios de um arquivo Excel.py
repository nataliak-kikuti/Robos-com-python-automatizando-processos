import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import openpyxl

print('Iniciando nosso robô... \n')
arquivo = open("resultado.txt","w")
driver = webdriver.Chrome()
driver.get("https://registro.br/")

dominios = []
workbook = openpyxl.load_workbook('lista.xlsx')
sheet = workbook.active  # Obtém a planilha ativa

for linha in range(1, 11):  #ler as 10 primeiras linhas
    valor = sheet.cell(row=linha, column=1).value  # Lê o valor da coluna A (coluna 1)
    dominios.append(valor)





for dominio in dominios:
    pesquisa = driver.find_element(By.ID, 'is-avail-field')
    pesquisa.clear()
    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(2)
    resultados = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/section/div[2]/div/p/span/strong').text
    texto = "Domínio %s %s" % (dominio, resultados)
    arquivo.write(texto)

arquivo.close()
driver.close()
