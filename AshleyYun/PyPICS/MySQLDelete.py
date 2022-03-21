import mysql.connector as mc

try:
    mydb = mc.connect(
        host="localhost",
        user="root",
        password="123456",
        database="ashley_pyqt"
    )

    mycursor = mydb.cursor()

    query = "DELETE FROM users WHERE email = 'dlfp@gmail.com'"

    mycursor.execute(query)

    mydb.commit()

    print(mycursor.rowcount, "record deleted")


except mc.Error as e:
    print("Deleting Failed")