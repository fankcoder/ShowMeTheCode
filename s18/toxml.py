#coding:utf-8
import json
import xlrd
from lxml import etree
data = xlrd.open_workbook('./city.xls')
table = data.sheets()[0]
nrows = table.nrows
dic = {}
for each in range(nrows):
    value = table.row_values(each)
    dic[value[0]] = value[1]

root = etree.Element('root')
child1 = etree.SubElement(root,'citys')
comm = etree.Comment(u'城市信息')
child1.append(comm)
child1.text = unicode(json.dumps(dic))
tree = etree.ElementTree(root)
tree.write('./city.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')
