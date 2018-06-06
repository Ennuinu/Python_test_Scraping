import urllib3
from bs4 import BeautifulSoup


html = urllib3.PoolManager()

request = html.request('GET', 'https://gadgetrip.jp/')
soup =  BeautifulSoup(request.data , 'html.parser')

for i in soup(['script', 'style']):
    i.decompose()

text = ' '.join(soup.stripped_strings)

print(text)