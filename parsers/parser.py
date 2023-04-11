from abc import ABC, abstractmethod


class IParser(ABC):

    @abstractmethod
    def parse(self, url):
        pass
