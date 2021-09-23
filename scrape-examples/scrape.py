import requests, bs4
# While beautifulsoup4 is the name used for 
# installation, to import Beautiful Soup 
# you run import bs4.

res = requests.get('https://nostarch.com') 
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser") 
# headers = (soup.select('h1')[0]).getText()
headers = []

for h2 in soup.select('h2'):
  headers.append(h2.getText())
print('\r\n'.join(headers))
# print(soup)