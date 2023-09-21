from openpyxl import Workbook

print("Inincinado nosso robo ...")
print("Lendo dados de arquivo de texto")

file = open('gastos.txt', 'r', encoding='utf-8')

arquivo = file.read()

lista_dados = arquivo.splitlines()

for i in range(0, len(lista_dados)):
    lista_dados[i] = lista_dados[i].split(",")

print("Criando arquivo excel ...")
wb = Workbook()
ws = wb.active

for row  in lista_dados:
    ws.append(row)

wb.save('gastos.xlsx')