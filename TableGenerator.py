'''
Created on 2018/04/19

@author: "KanesuSota"
'''

import xlrd

book = xlrd.open_workbook("sample.xlsx")
sheet = book.sheet_by_index(0)

f = open("text.txt", "w")

#各行をlist
x = []
for row in range(sheet.nrows):
    y = []
    for col in range(sheet.ncols):
        y.append(sheet.cell(row, col).value)
    x.append(y)

print(x)

#1行ずつ出力
for i in x:
    for j,k in enumerate(i):
        if j == len(i)-1:
            f.write(k + "\n")
        else:
            f.write(k+ ", ")
f.close()