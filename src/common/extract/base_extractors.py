import requests
from abc import ABC, abstractmethod

from common.logger.logger import get_logger

logger = get_logger(__name__)

class Extractor(ABC):

    @abstractmethod
    def extract(self):
        pass

class ApiExtraction(Extractor):

    def __init__(self, url):
        self.url = url

    def extract(self) -> int :
        try:
            response = requests.get(self.url)

            logger.info(f"Succesfully conection from {self.url}")
        except Exception as e:

            logger.error(f"Fail conection from {self.url} with this error {e}")

        return response.status_code,response


