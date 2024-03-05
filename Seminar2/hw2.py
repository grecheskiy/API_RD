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
books = soup.find_all('article', {'class':'product_pod'})
for book in books:
    book_info = {}
    name_info = book.find('img', {'class':'thumbnail'})
    book_info['name'] = name_info.get('alt')
    price_info = book.find('p', {'class':'price_color'})
    book_info['price'] = float(price_info.getText()[2:])