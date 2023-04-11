from browser.browser import IBrowser
from selenium import webdriver


class Browser(IBrowser):

    def __init__(self, url):
        self.url = url
        self.driver = None
        self.html = None

    def _init_driver(self, browser: str) -> None:
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
        elif browser == "Firefox":
            self.driver = webdriver.Firefox()

    def start(self, browser: str) -> None:
        self._init_driver(browser)
        self.driver.get(self.url)
        self.html = self.driver.page_source

    def stop(self) -> None:
        self.driver.quit()