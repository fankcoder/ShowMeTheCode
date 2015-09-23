import random,string

def randChoice(num,length=8):
    f = open('activation.txt','w')
    for each in range(num):
        randStrs = ''
        randStr = string.letters+string.digits
        s = [random.choice(randStr) for i in range(length)]
        f.write(''.join(s)+'\n')
        f.close

randChoice(200)
