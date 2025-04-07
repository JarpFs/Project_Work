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


def main() -> None:


    #URL de la API pública (JSONPlaceholder)
    url = 'https://jsonplaceholder.typicode.com/posts'

    api_call = ApiExtraction(url)

    status, response = api_call.extract()

    # Realizar una solicitud GET para obtener los datos
    #response = requests.get(url)

    # Verificar que la solicitud fue exitosa
    if status == 200:
        # Convertir la respuesta JSON a un diccionario de Python
        data = response.json()
        logger.info(f"Datos recibidos: {data[:5]}")  # Imprimir los primeros 5 elementos
    else:
        logger.error(f"Error al hacer la solicitud. Código de estado: {response.status_code}")

if __name__ == "__main__":
    main()