import mysql.connector as mc

try:
    mydb = mc.connect(
        host="localhost",
        user="root",
        password="123456",
        database="ashley_pyqt"
    )

    mycursor = mydb.cursor()

    query = "UPDATE users SET email = 'dlfp@gmail.com' WHERE email = '33'"

    mycursor.execute(query)

    mydb.commit()

    print(mycursor.rowcount, "record affected")


except mc.Error as e:
    print("Updating Failed ")