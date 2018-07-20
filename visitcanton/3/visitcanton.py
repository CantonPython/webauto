from selenium.webdriver import Firefox, FirefoxOptions

options = FirefoxOptions()
options.set_headless()

try:
    print('> starting firefox...')
    browser = Firefox(options=options)
    print('> getting the page...')
    browser.get('https://www.visitcanton.com/event-calendar/')
    element = browser.find_element_by_id('events-directory')
    text = element.text
    print('> events-directory text')
    print(text)
finally:
    browser.quit()
