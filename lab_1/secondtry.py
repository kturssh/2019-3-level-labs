from bs4 import BeautifulSoup
import requests
import re
import json
import datetime


def get_html_page(page_url='http://ru-good.ru/category/science'):
    our_doc = requests.get(page_url)
    our_constant = our_doc.text
    if our_doc.status_code == 200:
        articles = find_articles(our_constant)
        publish_report(page_url, articles)
    else:
        print("oops")
    return our_constant


def find_articles(our_constant):
    parc_page = BeautifulSoup(our_constant, 'html.parser')
    title = parc_page.find_all("h2")
    parsed_content = []
    for parsed in title:
        parsed_content.append({'title': parsed.get_text()})
    return parsed_content
  

def publish_report(path, articles):
    print("report")
    our_file = {'url': path, 'creationDate': datetime.datetime.now().strftime("%Y-%m-%d"), 'articles': articles}
  
    with open('articles.json', "w", encoding='utf-8') as file:
        json.dump(our_file, file, indent=2, ensure_ascii=False)


get_html_page('http://ru-good.ru/category/science')
