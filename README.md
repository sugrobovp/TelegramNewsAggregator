# Telegram News Aggregator
### Описание
Данный проект агрегирует новости с сайтов и пересылает их по телеграм боту конечному пользователю. 
Предназначен для того, чтобы все новости могли быть прочитаны в одном месте, и пользователю не пришлось
бы прыгать по разным ресурсам
### Зависимости
В данном проекте используется библиотека BeautifulSoup для парсинга сайтов, не имеющих внешнего API.
Так же используется Selenium для имитации работы различных браузеров. Для работы с Telegram API
используется пакет telegram-bot
### Реализация
Для того чтобы уменьшить зависимость от конкретных реализаций, было решено сделать абстрактные интерфейсы
для имитации работы браузера и парсера
```python
class IBrowser(ABC):

    @abstractmethod
    def start(self, browser: str) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass

class IParser(ABC):

    @abstractmethod
    def parse(self):
        pass
```
Таким образом удалось добиться соблюдения DIP (Dependency Inversion Principle) и уменьшить связанность
между различными компонентами проекта.

Как уже говорилось, в данном проекте для реализации IBrowser было решено пользоваться
Selenium, а для IParser - BeautifulSoup

### Использование
Необходимо запустить telegram_bot.py, в котором требуется указать личный chat_id 
и токен бота Telegram, чтобы пользователю приходили сообщения. Есть возможность настроить периодичность
сообщений. Для добавления новых сайтов, необходимо писать реализации парсеров под каждый конкретный сайт. Так как
html код разных ресурсов разный.

### Дальнейшее расширение
При дальнейшем расширении и увеличении нагрузки на проект, может понадобиться асинхронное выполнение тяжелых парсингов.
Для этого можно использовать Celery в качестве асинхронного обработчика задач и Redis в качестве
брокера сообщений для Celery.