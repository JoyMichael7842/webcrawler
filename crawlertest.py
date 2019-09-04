import mysql.connector
from bs4 import BeautifulSoup
import urllib.request

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "atgworld",
	database = "joy"
)
mycursor = mydb.cursor()


url = "https://dmoz-odp.org"
resp = urllib.request.urlopen(url)
soup = BeautifulSoup(resp,features="lxml", from_encoding=resp.info().get_param('charset'))

count = 0;
sqlformula = "INSERT INTO webcrawler (linkid, links) VALUES (%s ,%s)"
for link in soup.find_all('a', href=True):
	string = str(link['href'])
	if string[0] == '/':
		string = url + string
	count = count+1
	var = (count,string)
	mycursor.execute(sqlformula,var)
	if count>45:
		break
	print(string)

mydb.commit()