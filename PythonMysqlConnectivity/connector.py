import mysql.connector as c
con = c.connect(host='localhost', user='root', passwd='arem00', database='temp')

if con.is_connected():
    print("Successfully connected")
else:
    print("Error")