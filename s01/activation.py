import random

def randChoice():
    randStrs = ''
    randStr = chr(random.randint(97,122))
    randInt = random.choice('0123456789')
    def choiceWord():
        rand = random.randint(0,1)
        if rand == 0:
            return randStr
        else:
            return randInt
    return choiceWord


f = open('activation.txt','w')
for item in range(0,200):
    randStrsNum = ''
    for each in range(0,8):
        randStrs = randChoice()
        randStrsNum = randStrsNum + randStrs()
    f.write(randStrsNum+'\n')
f.close()
