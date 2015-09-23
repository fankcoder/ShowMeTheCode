import redis

def codeRedis():
    r = redis.Redis(host='localhost',port=6379,db=0)
    f = open('activation.txt','rb')
    num = 0
    for iteam in f.readlines():
        iteam = iteam.strip()
        r.lpush(num,iteam)
        num = num +1
    f.close()

if __name__=='__main__':
    codeRedis()
