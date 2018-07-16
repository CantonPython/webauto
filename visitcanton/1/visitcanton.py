import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.visitcanton.com/events-calendar/')
result.raise_for_status()

soup = BeautifulSoup(result.content, 'html.parser')
print('---- html ----')
print(soup.prettify())
