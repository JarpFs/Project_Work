import requests
from abc import ABC, abstractmethod
from typing import Union


from common.logger.logger import get_logger

logger = get_logger(__name__)

class Extractor(ABC):

    @abstractmethod
    def extract(self):
        pass

class ApiExtraction(Extractor):

    def __init__(self, url):
        self.url = url

    def extract(self) -> tuple[int, Union[dict, list, None]]:
        try:
            response = requests.get(self.url)
            response.raise_for_status() 

            logger.info(f"Succesfully conection from {self.url}")
            return response.status_code, response.json()

        except requests.RequestException as e:

            logger.error(f"Fail conection from {self.url} with this error {e}")
            return None, None


