from abc import ABC, abstractmethod


class IBrowser(ABC):

    @abstractmethod
    def start(self, browser: str) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass
