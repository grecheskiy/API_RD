# Задание 2
# Напишите сценарий, чтобы получить ссылки на релизы фильмов со страницы на сайте
# Сохраните ссылки в списке и выведите список на консоль

# Использовать библиотеку requests для запроса веб-страницы
# Использовать BeautifulSoup для парсинга HTML-содержимого веб-страницы
# Найти все ссыоки в колонке №1 Release веб-страницы
# Используйте библиотеку urllib.parse для объединения ссылок с базовыми urlСохраните ссылки в списки и выведите список в консоль

import requests
from bs4 import BeautifulSoup
import urllib.parse

url = 'https://www.boxofficemojo.com/intl/?ref_=bo_nb_hm_tab'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

realease_links = []
for link in soup.find_all('td', {"class":"a-text-left mojo-field-type-release mojo-cell-wide"}):
    atag = link.find('a')
    if atag:
        realease_links.append(atag.get('href'))
print(realease_links)

url_join = [urllib.parse.urljoin('https://www.boxofficemojo.com', link) for link in realease_links]
print(url_join)
