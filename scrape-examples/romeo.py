import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
# type(res)
# res.status_code == requests.codes.ok
# http:// requests.readthedocs.org/.
try:
  res.raise_for_status() 
  print(res.text[:250])
  playFile = open('RomeoAndJuliet.txt', 'wb')
  for chunk in res.iter_content(100000):
    playFile.write(chunk)
  playFile.close()
except Exception as exc:
  print('There was a problem: %s' % (exc))