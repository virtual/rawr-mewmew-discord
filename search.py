import requests, bs4, sys, os
from dotenv import load_dotenv
import pyinputplus as pyip

load_dotenv()

RANKS_URL =  os.getenv('RANKS_URL')
CHAR_URL =  os.getenv('CHAR_URL')
ranktype = pyip.inputMenu(['levels', 'fame'], numbered=True)
ign = pyip.inputStr(prompt='Enter a IGN: ')

url = RANKS_URL
if (ranktype != 'levels'):
  url = RANKS_URL + ranktype
  res = requests.post(url, data = {'search': ign})
  res.raise_for_status()
  soup = bs4.BeautifulSoup(res.text, "html.parser") 
  # headers = (soup.select('h1')[0]).getText()
  users = []
  rank = '0' # fix this with destructuring?
  # td:nth-child(3) > a > b, 
  for user in soup.select('td:nth-child(3) > a > b'):
    users.append(user.getText() + ' - ' + rank)
  print('\r\n'.join(users))
else:
  url = CHAR_URL + ign
  res = requests.get(url)
  res.raise_for_status()
  soup = bs4.BeautifulSoup(res.text, "html.parser") 
  for line in soup.select('.col-md-9 .well'):
    print(line.getText())
