from browser.implementations import Browser
from parsers import BeautifulSoupHTMLParser, CybersportParser
import telegram


url = 'https://www.cybersport.ru/'


def get_data():
    browser = Browser(url=url)
    a = BeautifulSoupHTMLParser(browser=browser, browser_type='Chrome')
    parser = CybersportParser(parser=a)
    data = parser.parse(url)
    return data


if __name__ == "__main__":
    url = "https://www.cybersport.ru/"
    data = get_data()
    print(data)