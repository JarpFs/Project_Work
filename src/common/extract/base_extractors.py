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

    def request(self, method: str = "get", **kwargs) -> requests.Response:
        method = method.lower()
        if method not in {"get", "post", "put", "delete", "patch"}:
            raise ValueError(f"Unsupported HTTP method: {method}")

        return requests.request(method, self.url, **kwargs)

    def extract(self,method: str = 'get', **kwargs) -> tuple[int, Union[dict, list, None]]:
        try:
            response = self.request(method, **kwargs)
            response.raise_for_status() 

            logger.info(f"Succesfully conection from {self.url}")

            if response.content and "application/json" in response.headers.get("Content-Type", ""):
                try:
                    data = response.json()
                except ValueError as e:
                    logger.warning(f"Could not decode JSON from {self.url}: {e}")
                    data = None
            else:
                logger.warning(f"No JSON content in response from {self.url}")
                data = None
            return response.status_code, response.json()

        except requests.RequestException as e:

            logger.error(f"Fail conection from {self.url} with this error {e}")
            return None, None


         




