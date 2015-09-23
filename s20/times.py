import xlrd
data = xlrd.open_workbook('phone.xls')
table = data.sheets()[0]
nrows = table.nrows
for each in range(nrows):
    value = table.row_values(each)
    print value[3]
