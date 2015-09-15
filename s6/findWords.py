import re
import os

num = 1
daily = 'daily/%s.txt' %num
f = open(daily,'r')
wordDict = f.read()
f.close()

words = re.findall(r'[a-zA-Z0-9]+',wordDict)
dic = {}
for word in words:
    time = 0
    for each in words:
        if each == word:
            time += 1
    dic[word]=time
print dic
