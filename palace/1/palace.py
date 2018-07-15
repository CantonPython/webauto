import requests

result = requests.get('https://www.cantonpalacetheatre.org/movies')
if result.status_code != 200:
    print('failed to get page: status', result.status_code)
else:
    print(result.content)
