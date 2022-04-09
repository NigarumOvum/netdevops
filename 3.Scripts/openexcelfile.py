import xlrd
import xlwt
import xlutils
#Code

def openexcelfile(self):
    book = xlrd.open_workbook(self)
    sheet = book.sheet_by_index(0)
    
