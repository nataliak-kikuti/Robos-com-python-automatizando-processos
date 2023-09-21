from openpyxl import load_workbook

file = 'book1.xlsx'

wb = load_workbook(filename=file)

ws = wb['Data']

ws.move_range("A2:Z2", rows=-1)


#Move F8 dua colunas para a direita
ws.move_range("F8:F8", cols=4)
#Move F10 dua colunas para a esquerda
ws.move_range("F10:F10", cols=-4)

#duas para a esquerda e uma para cima
ws.move_range("C13:E15", cols=-2, rows=-1)


wb.save("book_celulas_movidas.xlsx")