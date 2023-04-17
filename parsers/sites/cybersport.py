from parsers.parser import IParser
from datetime import datetime


class CybersportParser:

    def __init__(self, parser: IParser):
        self.parser = parser

    def parse(self):
        soup = self.parser.parse()
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

            try:
                img = block.find('img')['src']
            except TypeError:
                img = 'Нету изображения'

            # Выводим извлеченную информацию
            results.append({
                'title': title,
                'link': link,
                'category': category,
                'date': pub_date,
                'img': img
            })

            print('Title:', title)
            print('Link:', link)
            print('Category:', category)
            print('Publication Date:', pub_date)
            print('img:', img)
            print()

        return results
