# coding: utf-8
#操作EXCEL，用于打开EXCEL文件，获取EXCEL的行，列等参数。
import xlrd
import xlwt
import xlutils
class excel():
    
#打开EXCEL文件,filename参数为EXCEL文件的名称及路径，Index参数为工作表的序号，0为第一个工作表。
    def __init__(self,filename,index):
        self.filename = filename
        self.workbook = xlrd.open_workbook(self.filename)
        sheets = self.workbook.sheet_by_index(index)
        self.sheets = sheets
        print('success')
        
#返回EXCEL工作表的总行数和总列数，变量ROWS为总行数，变量COLUMNS为总列数。
    def getRowsColsNum(self):
        rows = self.sheets.nrows
        columns = self.sheets.ncols
        return rows,columns
        print('总行数为：'+ rows,'总列数为:' + columns)
        
#返回某个单元格的值，ROW为第几行，COLUMN为第几列，参为0，0为EXCEL表的A1单元格。
    def getCellValues(self,row,column):
        cellvalues = self.sheets.cell(row,column).value
        return cellvalues
        print(cellvalue)
        
#返回某行的内容，ROW参数为0到最大行数-1。
    def getRowValues(self,row):
        rowvalues = self.sheets.row_values(row)
        return rowvalues
        print(rowvalues)
        
#返回某列的内容，COL参数为0到最大列数-1。
    def getColumnValues(self,col):
        colvalues = self.sheets.col_values(col)
        return colvalues
        print(colvalues)
        
#返回所有行的内容。
    def getAllRowsValues(self):
        row = self.sheets.nrows
        rowdata = []
        for i in range(row):
            rows = self.sheets.row_values(i)
            rowdata.append(rows)
        return(rowdata)
        print(rowdata)
            
    