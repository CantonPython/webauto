import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.cantonpalacetheatre.org/movies')
result.raise_for_status()

soup = BeautifulSoup(result.content, 'html.parser')
print('---- html ----')
print(soup.prettify())
print('---- text ----')
print(soup.get_text())
