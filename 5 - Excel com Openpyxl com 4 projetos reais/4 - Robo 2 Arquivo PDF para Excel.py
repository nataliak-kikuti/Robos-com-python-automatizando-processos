import PyPDF2
from openpyxl import Workbook

pdf_file = open("gastos.pdf", "rb")

read_pdf = PyPDF2.PdfReader(pdf_file)

page = read_pdf.pages[0]

page_content = page.extract_text()
parsed = page_content.splitlines()
print(parsed)
