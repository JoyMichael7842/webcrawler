import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "Password@7842",
	database = "testdb"
)

mycursor = mydb.cursor()

sqlformula = "INSERT INTO students (name,age) VALUES (%s,%s)"
student1 =("Rachel",22)

mycursor.execute(sqlformula,student1)

mydb.commit()