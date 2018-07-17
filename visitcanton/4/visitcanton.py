from __future__ import print_function
from selenium.webdriver import Firefox, FirefoxOptions
from bs4 import BeautifulSoup

options = FirefoxOptions()
options.set_headless()

browser = Firefox(options=options)
browser.get('https://www.visitcanton.com/event-calendar/')
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())
browser.close()
