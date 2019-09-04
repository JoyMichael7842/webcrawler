import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "atgworld",
	database = "joy"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * from webcrawler")

myresult = mycursor.fetchall()

for row in myresult:
	print(row)