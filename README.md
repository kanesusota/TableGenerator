# TableGenerator
pythonでExcelからなんか作る

## 準備
読み込みにはxlrdを使う

インストール方法は
```
pip install xlrd
```

## xlrd
### ブックのオープン
```
import xlrd
 
book = xlrd.open_workbook('sample.xlsx')
```

### シートの取得
```
sheet = book.sheet_by_index(0)
```

### セル値の取得
cellの引数に行と列を指定する。
```
for col in range(sheet.ncols):
    for row in range(sheet.nrows):
        print(sheet.cell(row, col).value)
```
