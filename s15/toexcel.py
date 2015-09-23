import xlwt
import json
with open('city.txt') as f:
    data = f.read()
    datajson = json.loads(data)
    exfile = xlwt.Workbook()
    table = exfile.add_sheet('city',cell_overwrite_ok=True)
    for each in range(3):
        table.write(each,0,str(each))
        table.write(each,1,datajson[str(each+1)])
    exfile.save('city.xls')

