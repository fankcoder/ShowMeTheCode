import re

f = open('pyDoc.txt','r') 
s = f.read()
f.close()
print len(re.findall(r'[a-zA-Z0-9]+',s))
