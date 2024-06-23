import os

import requests
from bs4 import BeautifulSoup
import json
from cloudscraper import create_scraper

output_dir = 'html_files'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

scraper = create_scraper()

# Получение HTML-страницы
url = "https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/"
response = scraper.get(url)

filename = os.path.join(output_dir, 'farpost.html')
with open(filename, 'w', encoding='utf-8') as file:
    file.write(response.text)

# Парсинг HTML
soup = BeautifulSoup(response.text, 'lxml')
s = soup.find("tr", class_="bull-list-item-js -exact map-highlighted")






"""# Получение заголовков объявлений
advertisements = []
for announcement in soup.find_all('div', class_='announcement'):
    title = announcement.find('h2', class_='announcement-title').text
    id = announcement.find('span', class_='announcement-id').text
    author = announcement.find('span', class_='announcement-author').text
    views = announcement.find('span', class_='announcement-views').text
    position = announcement.find('span', class_='announcement-position').text

    # Создание модели данных
    advertisement = {
        'title': title,
        'id': id,
        'author': author,
        'views': views,
        'position': position
    }
    advertisements.append(advertisement)

# Сохранение данных в файл test_ads.json
with open('test_ads.json', 'w', encoding='utf-8') as file:
    json.dump(advertisements, file, ensure_ascii=False, indent=4)"""
