import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.visitcanton.com/events-calendar/day/2018/07/21/')
result.raise_for_status()

soup = BeautifulSoup(result.content, 'html.parser')
print('---- html ----')
print(soup.prettify())
