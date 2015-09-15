#coding:utf-8
import os
import sys
import re

fankfile = sys.argv[1]
dirlist = os.listdir(fankfile)
time = 0
parttern = re.compile(r'.+py\Z')
parttern2 = re.compile(r'\A#.*')
emptyList,noteList,codeList = [],[],[] 

def total(fileName):
    emptyNum,noteNum,codeNum = 0,0,0
    f = open(fileName)
    #num = 0
    lines = f.readlines()
    #if k
    f.close()
    #print lines
    for each in lines:
        if each == '\n':
            emptyNum += 1
        elif re.findall(parttern2,each):
            noteNum += 1
        else:
            codeNum += 1
    emptyList.append(emptyNum)
    noteList.append(noteNum)
    codeList.append(codeNum)

for each in dirlist:
    time += 1
    #目录或文件
    direach = os.path.join(fankfile,each)
    if os.path.isdir(direach) == True:   
        #二级目录
        for each in os.listdir(direach):
            p = parttern.findall(each)
            if p:
                #total(p[0])
                total(os.path.join(direach,each))
                #total('/home/icgoo/pywork/show_me_the_code/s0/s0_image.py')
    #py文件
    else:
        p = parttern.findall(each)
        if p:
            pyPath = os.path.join(fankfile,p[0])
            total(pyPath)

def plus():
    emptySum = reduce(lambda x,y:x+y,emptyList)
    noteSum = reduce(lambda x,y:x+y,noteList)
    codeSum = reduce(lambda x,y:x+y,codeList)
    print '您留出的空行为:',emptySum
    print '您的备注行为:',noteSum
    print '您的总代码行数为:',codeSum
    
if __name__ == '__main__':
    plus()
