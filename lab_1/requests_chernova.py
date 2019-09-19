import requests

page_url = 'https://lenta.ru/rubrics/sport'

lenta_sport_request = requests.get(page_url)

if lenta_sport_request.status_code == 200:
  print(lenta_sport_request.text)
  print('We performed a successful request')
else:
  print('Something went wrong')