import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.cantonpalacetheatre.org/movies')
result.raise_for_status()

soup = BeautifulSoup(result.content, 'html.parser')

print('---- all links ----')
for link in soup.find_all('a'):
    print(link.text, link.get('href'))

print('---- main links ----')
div = soup.find(id='main')
for link in div.find_all('a'):
    print(link.text, link.get('href'))
