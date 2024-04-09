#Получить список 20 последний опубликованных объявлений о продаже автомобилей на сайте https://auto.drom.ru/,
#результат записать в файл.
from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests

def parse():
    url = 'https://auto.drom.ru/' # передаем необходимы URL адрес
    page = requests.get(url)  # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4
    block = soup.findAll('div', class_='css-jlnpz8 e1icyw250')  # находим  контейнер с нужным классом
    description = ''
    file = open('car_ads.txt', 'w', encoding='UTF-8')
    for data in block:
        if data.find('div'):
            description += data.text.strip() + '\n'
    print(description)
    file.write(description)
    file.close()
parse()
