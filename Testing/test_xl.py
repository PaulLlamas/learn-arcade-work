from openpyxl import Workbook
import random

work_book = Workbook()

work_sheet = work_book.active

work_sheet['A1'] = "This is a test"

for i in range(200):
    work_sheet.append(["Random Number:", random.randrange(1000)])

work_book.save("sample.xlsx")