import mysql.connector as mc

try:
    dbname = input("Please Enter Database Name : ")
    tablename = input("Please Enter Table Name : ")

    mydb = mc.connect(

        host="localhost",
        user="root",
        password="123456",
        database=dbname

    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM {} ".format(tablename))

    result = mycursor.fetchall()

    for data in result:
        print(data)


except mc.Error as e:
    print("Error")