from datetime import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
from typing import Type


# class Browser:
#
#     def __init__(self, url):
#         self.url = url
#         self.driver = webdriver.Chrome()
#         self.html = None
#
#     def start(self):
#         self.driver.get(self.url)
#         self.html = self.driver.page_source
#
#     def stop(self):
#         self.driver.quit()


class ParserInterface(ABC):

    @abstractmethod
    def parse(self, url):
        pass


class BeautifulSoupHTMLParser(ParserInterface):

    @classmethod
    def parse(cls, url):
        driver = webdriver.Chrome()
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        driver.quit()
        return soup


class CybersportParser:

    def __init__(self, parser: Type[BeautifulSoupHTMLParser]):
        self.parser = parser

    def parse(self, url):
        soup = self.parser.parse(url=url)
        data = self.extract_data(soup)
        return data

    @staticmethod
    def extract_data(soup):
        news_blocks = soup.find_all('div', class_='rounded-block root_d51Rr with-hover no-padding no-margin')

        results = []

        # Проходим по каждому блоку и извлекаем необходимую информацию
        for block in news_blocks:
            # Находим заголовок новости
            title = block.find('h3', class_='title_nSS03').text.strip()

            # Находим ссылку на новость
            link = block.find('a', class_='link_CocWY')['href']
            if not link.startswith('https://www.cybersport.ru'):
                link = 'https://www.cybersport.ru' + link

            # Находим категорию новости
            category = block.find('a', class_='tag_9QLmg').text.strip()

            # Находим дату публикации новости
            date_str = block.find('time')['datetime'].strip()
            pub_date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')

            # Выводим извлеченную информацию
            results.append({
                'title': title,
                'link': link,
                'category': category,
                'date': pub_date
            })

            print('Title:', title)
            print('Link:', link)
            print('Category:', category)
            print('Publication Date:', pub_date)
            print()

        return results
