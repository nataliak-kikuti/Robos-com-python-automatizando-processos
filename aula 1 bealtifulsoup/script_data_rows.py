from bs4 import BeautifulSoup


html_file = open("data_in_table.html",mode="r", encoding="utf-8")

soup = BeautifulSoup(html_file, "html.parser")

table = soup.find(id="main_table")
table_rows = table.find_all("tr")

dados_alunos = []

for linha in table_rows:
    colunas = linha.find_all("td")
    if len(colunas) > 0:
      codigo_estudante = colunas[0].text
      nome_estudante = colunas[1].text
      nota_estudante = colunas[2].text

      dict_aluno ={
         "codigo": codigo_estudante,
         "nome": nome_estudante,
         "nota": nota_estudante
      }
      dados_alunos.append(dict_aluno)
      print(f"{codigo_estudante} - {nome_estudante} - {nome_estudante}")


print(dados_alunos)

import pdb; pdb.set_trace()