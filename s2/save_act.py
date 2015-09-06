import MySQLdb

f = open('activation.txt','r')
lines = f.readlines()
f.close()
conn = MySQLdb.connect(host='localhost',user='root',passwd='****',db='showmethecode')
cursor = conn.cursor()
for line in lines:
    line = line.strip()
    cursor.execute("""INSERT INTO activation(code) VALUES ('%s');""" %line)
conn.commit()
cursor.close()
conn.close()
