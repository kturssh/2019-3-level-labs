import requests

from bs4 import BeautifulSoup

page_url = 'https://lenta.ru/rubrics/sport'

lenta_sport_request = requests.get(page_url)

lenta_sport_content = lenta_sport_request.text

if lenta_sport_request.status_code == 200:
  # print(lenta_sport_content)
  print('We performed a successful request')
else:
  print('Something went wrong')
  
parsed_page = BeautifulSoup(lenta_sport_content)

print(type(parsed_page))

print(parsed_page.title)