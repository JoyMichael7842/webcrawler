import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "atgworld",
	database = "joy"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE webcrawler (linkid INTEGER(10), links VARCHAR(255))")