import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="muniraja@256")
mycursor=mydb.cursor()

mycursor.execute('show databases')


