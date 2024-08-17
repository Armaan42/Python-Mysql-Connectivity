import mysql.connector as c
con = c.connect(host='localhost', user='root', passwd='arem00', database='temp')
cursor = con.cursor()

code = int(input("Enter the code: "))
query = "delete from mytable where code ={}".format(code)

cursor.execute(query)
con.commit()
if cursor.rowcount > 0:
    print("Deletion OK")
else:
    print("Error")

