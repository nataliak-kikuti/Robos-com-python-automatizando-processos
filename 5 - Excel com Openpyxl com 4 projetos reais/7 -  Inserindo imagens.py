from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active

ws['A1'] = "Voce vai ver uma imagem abaixo"

img = Image("python.png")

ws.add_image(img, 'A2')

wb.save(filename="logo.xlsx")
