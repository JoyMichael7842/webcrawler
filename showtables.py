import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "Password@7842",
	database = "joy"
)
mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for tb in mycursor:
	print(tb)