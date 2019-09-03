from bs4 import BeautifulSoup
import urllib.request

url = "https://dmoz-odp.org"
resp = urllib.request.urlopen(url)
soup = BeautifulSoup(resp,features="lxml", from_encoding=resp.info().get_param('charset'))

count = 0;
for link in soup.find_all('a', href=True):
	string = str(link['href'])
	if string[0] == '/':
		string = url + string
	count = count+1
	if count>45:
		break
	print(string)