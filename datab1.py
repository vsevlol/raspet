import mysql.connector
from mysql.connector import Error


import mysql.connector

conn = mysql.connector.connect(
         user='root',
         password='lizard',
         host='localhost',
         database='tele')


cur = conn.cursor()
