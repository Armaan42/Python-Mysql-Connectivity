import mysql.connector as c
con = c.connect(host='localhost', user='root', passwd='arem00', database='temp')
cursor = con.cursor()

while True:
    code = int(input("Enter the code: "))
    name = input("Enter the name: ")
    query = "insert into mytable values({},'{}')".format(code, name)
    cursor.execute(query)
    con.commit()
    print("Data inserted successfully")
    x = int(input("1_Enter more: \n2_Exit\nEnter the choice: "))
    if x == 2:
        break