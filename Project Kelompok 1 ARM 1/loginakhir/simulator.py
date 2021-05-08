import mysql.connector
import random, datetime, time

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="qwerty1234",
  database="sensor"
)
mycursor = mydb.cursor()

def Menu():
    print("SIMULATOR MESIN")
    print("1. Memasukkan data simulasi motor berulang")
    print("2. Memasukkan data simulasi hvac berulang")
    print("3. Memasukkan data simulasi pompa berulang")
    print("4. Memasukkan data simulasi motor, hvac, pompa bersamaan secara berulang")
    print("---------------------")
    print("5. Exit Program")
    print()
    choice = int(input("Enter here: "))

    if(choice==1):
        for i in range(50):
            now = datetime.datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            time.sleep(1.5)
            temperature = random.randint(50,70)
            status = "ON"
            
            mycursor = mydb.cursor()
            mycursor.execute("INSERT INTO motor (time, temp, status) VALUES (%s, %s, %s)", (time, temp, status))
            mydb.commit()
            print(mycursor.rowcount, "record kondisi motor dimasukkan.") Menu()
