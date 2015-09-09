import MySQLdb

f = open('activation.txt','r')
lines = f.readlines()
f.close()
<<<<<<< HEAD
conn = MySQLdb.connect(host='localhost',user='root',passwd='****',db='showmethecode')
=======
conn = MySQLdb.connect(host='localhost',user='root',passwd='*****',db='showmethecode')
>>>>>>> 643e3448f12032d0dacdcd7014d5b7558a72b879
cursor = conn.cursor()
for line in lines:
    line = line.strip()
    cursor.execute("""INSERT INTO activation(code) VALUES ('%s');""" %line)
conn.commit()
cursor.close()
conn.close()
