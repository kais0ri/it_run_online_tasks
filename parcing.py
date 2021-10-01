import requests
from bs4 import BeautifulSoup as BS
                # BeautifulSoup - это библиотека,
                # которая отвечает за манипуляцию данных
                # ( добавление, удаление и изменение )

# Счетчик
page = 1

while True:
                # Запрос на получение данных по указанному url адресу
    result = requests.get("https://stopgame.ru/review/new/izumitelno/p" + str(page))
                                # html.parser - это встроенный син. анализатор Python

    html = BS(result.content, 'html.parser') # Создание BS объекта

    items = html.select(".items > .article-summary") # Выбор (получение) данных с указанного css секлектора

    if len(items):
        for element in items:
            title = element.select(".caption > a")
            print(title[0].text)
        with open('parsing.txt','a') as f:
            f.write(title[0].text)
        page = page + 1

    else:
        break








