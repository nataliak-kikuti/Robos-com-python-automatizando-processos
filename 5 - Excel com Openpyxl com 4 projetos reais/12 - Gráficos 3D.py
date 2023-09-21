from openpyxl import Workbook
from openpyxl.chart import (AreaChart3D, Reference, Series)

wb = Workbook()
ws = wb.active

rows = [
    ['Ano', 'Lucro', 'Custos'],
    [2015, 40, 40],
    [2016, 25, 40],
    [2017, 30, 50],
    [2018, 10, 30],
    [2019, 5, 25],
    [2020, 10, 50]

]

for row in rows:
    ws.append(row)

chart = AreaChart3D()
chart_title = "Lucros x Custos"
chart.style = 13
chart.x_axis.title = "Ano"
chart.y_axis.title = "Porcentagem"

categoria = Reference(ws, min_col=1, min_row=1, max_row=6)
dados = Reference(ws, min_col=2, min_row=1, max_col=3, max_row=6)

chart.add_data(dados, titles_from_data=True)
chart.set_categories(categoria)


ws.add_chart(chart, 'A10')
wb.save(filename='chart3d.xlsx')