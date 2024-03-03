# Задание 3
# В консоли разработчика браузера найдите таблицу с данными и изучите ее HTML-структуру
# Напишите сценарий для запроса веб-страницы и парсинга содержимого с помощью библиотеки Beautiful soup
# Извлеките данные из таблицы и сохраните их в списке словарей, где каждый словарь представляет строку данных
# Преобразуйте список словарей в pandas Dataframe и выведите его в консоль

import requests
from bs4 import BeautifulSoup
import urllib.parse
import pandas as pd

url = 'https://www.boxofficemojo.com/intl/?ref_=bo_nb_hm_tab'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# realease_links = []
# for link in soup.find_all('td', {"class":"a-text-left mojo-field-type-release mojo-cell-wide"}):
#     atag = link.find('a')
#     if atag:
#         realease_links.append(atag.get('href'))
# print(realease_links)

# url_join = [urllib.parse.urljoin('https://www.boxofficemojo.com', link) for link in realease_links]
# print(url_join)

table = soup.find('table', {'class': 'a-bordered'})
headers = [header.text.strip() for header in table.find_all('th') if header.text]

data = []
for row in table.find_all('tr'):
    rowdata = {}
    cells = row.find_all('td')
    if cells:
        #rowdata[headers[0]] = cells[0].find('a').text if cells[0].find('a') else ''
        rowdata[headers[0]] = cells[0].text if cells[0].find('a') else ''
        rowdata[headers[1]] = cells[1].text
        rowdata[headers[2]] = cells[2].text
        rowdata[headers[3]] = cells[3].text
        rowdata[headers[4]] = cells[4].text.strip()
        rowdata[headers[5]] = cells[5].text.replace('$', '')   
        data.append(rowdata)
 #       print(data)

df = pd.DataFrame(data)
print(df)