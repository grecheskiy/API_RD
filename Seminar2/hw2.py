# Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/ 
# и извлечь информацию о всех книгах на сайте во всех категориях: 
# название, цену, количество товара в наличии (In stock (19 available)) в формате integer, описание.
# Затем сохранить эту информацию в JSON-файле.

import requests
from bs4 import BeautifulSoup
import json
import urllib.parse
import pandas as pd

url = 'http://books.toscrape.com'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
#print(soup.prettify())

# data = []
# for link in soup.find_all('li', {'class': "col-xs-6 col-sm-4 col-md-3 col-lg-3"}):
#     atag = link.find('a')
#     if atag:
#         data.append(atag.get('href'))
# #print(data)
# url_join = [urllib.parse.urljoin('http://books.toscrape.com', link) for link in data]
# #print(url_join)

table =soup.find('div', {'class': "row"})
print(table.prettify())