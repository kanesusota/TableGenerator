'''
Created on 2018/04/19

@author: "KanesuSota"
'''

import xlrd

book = xlrd.open_workbook("sample.xlsx")
sheet = book.sheet_by_index(0)

f = open("text.txt", "w")

for col in range(sheet.ncols):
    for row in range(sheet.nrows):
        print(sheet.cell(row, col).value)

f.write(sheet.cell(0,0).value)
f.close()