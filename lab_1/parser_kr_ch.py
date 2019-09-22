from bs4 import BeautifulSoup
import requests
import re



page_url ='http://ru-good.ru/category/science'
ourdoc = requests.get(page_url)
our_constant = ourdoc.text
soup = BeautifulSoup(our_constant, 'html.parser')

# название статьи

title = soup.find("h2", {"class": re.compile("^page_title$")})
title =title.contents[0].string
with open('file.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join([title]))
    