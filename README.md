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
