import requests, bs4, sys, os
from dotenv import load_dotenv

load_dotenv()
# While beautifulsoup4 is the name used for 
# installation, to import Beautiful Soup 
# you run import bs4.
RANKS_URL =  os.getenv('RANKS_URL')
url = RANKS_URL + 'fame'
print(url)
res = requests.post(url, data = {'search': 'flowy'})
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser") 
# headers = (soup.select('h1')[0]).getText()
users = []
rank = '0' # fix this with destructuring?
# td:nth-child(3) > a > b, 
for user in soup.select('td:nth-child(3) > a > b'):
  users.append(user.getText() + ' - ' + rank)
  # headers.append(.getText())
print('\r\n'.join(users))