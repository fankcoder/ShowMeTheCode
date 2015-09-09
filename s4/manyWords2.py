import re

def count(filepath):
    f = open(filepath,'r') 
    s = f.read()
    f.close()
    return len(re.findall(r'[a-zA-Z0-9]+',s))

if __name__ == '__main__':
    num = count('pyDoc.txt')
    print num
