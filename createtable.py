import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "Password@7842",
	database = "joy"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE webcrawler (linkid INTEGER(10), links VARCHAR(255))")