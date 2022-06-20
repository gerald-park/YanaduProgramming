import mysql.connector as mc

try:
    mydb = mc.connect(

        host="localhost",
        user="root",
        password="123456",
        database="ashley_pyqt"

    )

    mycursor = mydb.cursor()

    email = input("Please Enter Your Email : ")
    password = input("Please Enter Your Password : ")

    query = "INSERT INTO users (email, password) VALUES (%s, %s)"
    value = (email, password)

    mycursor.execute(query, value)

    mydb.commit()
    print("Data Inserterd")



except mc.Error as e:
    print("Unable To Insert Data")