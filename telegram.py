from scrapper import CybersportScrapper, Browser
import telegram

browser = Browser(url='https://www.cybersport.ru/')
browser.start()


logic = CybersportScrapper()
print(logic.get_news())

