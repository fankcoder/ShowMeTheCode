#coding:utf-8
import json
import os
import xlrd
from lxml import etree
path = os.path.split(os.path.realpath(__file__))[0]+'/'
data = xlrd.open_workbook(path+'numbers.xls')
table = data.sheets()[0]
nrows = table.nrows
List = []
for each in range(nrows):
    value = table.row_values(each)
    List.append(value)
root = etree.Element("root")
child1 = etree.SubElement(root, "numbers")
comm = etree.Comment(u"""数字信息""")
child1.append(comm)
child1.text =unicode(json.dumps(List).decode("utf-8"))
tree = etree.ElementTree(root)    
tree.write(path+"numbers.xml ", pretty_print=True, xml_declaration=True, encoding='utf-8') 
