import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.cantonpalacetheatre.org/movies')
result.raise_for_status()

soup = BeautifulSoup(result.content, 'html.parser')

table = soup.table
for tr in table.find_all('tr'):
    image,title,date,time = tr.find_all('td')
    print('title:', title.string)
    print('date:', date.string)
    print('time:', time.text.strip())
    print('-- ')
