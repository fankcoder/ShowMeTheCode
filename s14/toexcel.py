import xlwt
import json
with open('students.txt') as f:
    data = f.read()
    datajson = json.loads(data)
    print datajson['1'][0]
    exfile = xlwt.Workbook()
    table = exfile.add_sheet('message',cell_overwrite_ok=True)
    for each in range(1,5):
        table.write(0,0,'1')
        table.write(1,0,'2')
        table.write(2,0,'3')
        table.write(0,each,datajson['1'][each-1])
        table.write(1,each,datajson['2'][each-1])
        table.write(2,each,datajson['3'][each-1])
    exfile.save('students.xls')
