from __future__ import print_function
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.visitcanton.com/event-calendar/')
element = browser.find_element_by_id('events-directory')
text = element.text
print(text)
