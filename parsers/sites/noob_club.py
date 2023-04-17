from parsers.parser import IParser
from datetime import datetime


class NoobClubParser:

    def __init__(self, parser: IParser):
        self.parser = parser

    def parse(self):
        soup = self.parser.parse()
        data = self.extract_data(soup)
        return data

    @staticmethod
    def extract_data(soup):
        news_blocks = soup.find_all('div', class_='entry first')

        results = []

        # Проходим по каждому блоку и извлекаем необходимую информацию
        for block in news_blocks:
            # Находим заголовок новости
            title = block.find('h1').find('a').text.strip()

            # Находим ссылку на новость
            link = block.find('h1').find('a')['href']
            if not link.startswith('https://www.noob-club.ru'):
                link = 'https://www.noob-club.ru' + link

            # Выводим извлеченную информацию
            results.append({
                'title': title,
                'link': link,
            })

            print('Title:', title)
            print('Link:', link)
            print()

        return results






