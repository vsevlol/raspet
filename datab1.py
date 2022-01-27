import datetime
import re
import calendar

import mysql.connector
from mysql.connector import Error


import mysql.connector
#def bazad:

now = datetime.datetime.now()

#@bot.message_handler(commands=['start'])

ye=int(now.year)
print(ye)
chas=int(now.hour)
min=int( now.minute)
print('chas=',chas)
print('min=',min)
mes=int(now.month)
chis=int(now.day)


nomden=calendar.weekday(ye,mes,chis)
kalen={}
kalen={0:"mondey",
         1:"tuesday",
         2:"wednesday",
         3:"thursday",
         4:"friday"}
den=kalen.get(nomden)





    
conn = mysql.connector.connect(
         user='root',
         #password='lizard',
         host='localhost',
         database='rasp')


cur = conn.cursor()
print("cur=",cur)
print('den=',den)
#query="SELECT * FROM %s WHERE chasi LIKE \"%" + chas +"%\" "
query = 'SELECT * FROM "%%%s" WHERE chasi LIKE "%%%s"'
#cur.execute(sql, (us,))

cur.execute(query,(den,),(chas,))
for (post) in cur:
  print(post)

    
