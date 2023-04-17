from parsers.parser import IParser
from browser import IBrowser
from bs4 import BeautifulSoup


class BeautifulSoupHTMLParser(IParser):

    def __init__(self, browser: IBrowser, browser_type: str):
        self.browser = browser
        self.browser_type = browser_type

    def parse(self):
        self.browser.start(self.browser_type)
        html = self.browser.driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        self.browser.stop()
        return soup
