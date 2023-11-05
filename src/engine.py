from abc import ABC, abstractmethod


class Engine(ABC):
    """Абстрактный класс получения данных по API"""

    @abstractmethod
    def get_request(self, keyword, count_page):
        pass

    @abstractmethod
    def get_vacancies(self, keyword, count_page):
        pass

    @abstractmethod
    def get_filtered_vacancies(self):
        pass
