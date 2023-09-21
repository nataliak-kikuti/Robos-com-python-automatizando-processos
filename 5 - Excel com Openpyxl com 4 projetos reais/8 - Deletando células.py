from openpyxl import load_workbook


nome_arquivo = "book.xlsx"

wb = load_workbook(filename=nome_arquivo)

ws = wb['Data']

ws.delete_rows(1)

wb.save(filename=nome_arquivo)
