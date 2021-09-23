import requests, bs4, sys, os
from dotenv import load_dotenv

load_dotenv()
# While beautifulsoup4 is the name used for 
# installation, to import Beautiful Soup 
# you run import bs4.
RANKS_URL =  os.getenv('RANKS_URL')
url = RANKS_URL
if len(sys.argv) > 1:
  url += sys.argv[1]
else:
  url += 'linked'
res = requests.get(url) 
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser") 
# headers = (soup.select('h1')[0]).getText()
headers = []

for h2 in soup.select('td > a > b'):
  headers.append(h2.getText())
print('\r\n'.join(headers))
# print(soup)