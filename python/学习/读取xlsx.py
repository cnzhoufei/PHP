import xlrd

workbook = xlrd.open_workbook('X站论坛.xlsx')

#总行数
table = workbook.sheets()[0]
count = table.nrows

print(workbook.sheet_by_index(0))
booksheet = workbook.sheet_by_index(0)  #或用名称取sheet
# print(booksheet)

#读单元格数据  
cell_11 = booksheet.cell_value(0,0)  
cell_21 = booksheet.cell_value(1,1)  
#读一行数据  

row_3 = booksheet.row_values(1)  #读取第一行
row_3 = booksheet.row_values(2,2)  #读取第二行 跳过两列
print(row_3)  