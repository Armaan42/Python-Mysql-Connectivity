import mysql.connector as c
con = c.connect(host='localhost', user='root', passwd='arem00', database='temp')
cursor = con.cursor()

query = "select * from mytable"
cursor.execute(query)

data = cursor.fetchall() #fetchone, fetchall, fetchmany
print(data)
print("Total no. of rows = ", cursor.rowcount)



