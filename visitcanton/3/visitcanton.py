from __future__ import print_function
from selenium.webdriver import Firefox, FirefoxOptions

options = FirefoxOptions()
options.set_headless()

print('> starting firefox...')
browser = Firefox(options=options)
print('> getting the page...')
browser.get('https://www.visitcanton.com/event-calendar/')
element = browser.find_element_by_id('events-directory')
text = element.text
print(text)
browser.close()
