import xlwt
import json
with open('numbers.txt') as f:
    data = f.read()
    datajson = json.loads(data)
    exfile = xlwt.Workbook()
    table = exfile.add_sheet('num',cell_overwrite_ok=True)
    #print datajson[0][0]
    for each in range(3):
        table.write(0,each,datajson[0][each])
        table.write(1,each,datajson[1][each])
        table.write(2,each,datajson[2][each])
    exfile.save('numbers.xls')
