
from common.logger.logger import get_logger
from common.extract.base_extractors import ApiExtraction
import os
from dotenv import load_dotenv
import pandas as pd


load_dotenv()

logger = get_logger(__name__)


def main() -> None:

    api_key = os.getenv('KEY_AEMET')

    #URL de la API pública (JSONPlaceholder)
    url = 'https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/estaciones/C419X'

    headers = {
        "accept": "application/json",
        "api_key": api_key
    }

    api_call = ApiExtraction(
        url
    )

    status, response = api_call.extract(
        method='get',
        headers = headers
    )

    # Verificar que la solicitud fue exitosa
    if status == 200:
        # Convertir la respuesta JSON a un diccionario de Python
        data = response
        logger.info(f"Datos recibidos (primeras 5 claves): {list(data.items())[:5]}") # Imprimir los primeros 5 elementos
    else:
        logger.error(f"Error al hacer la solicitud. Código de estado: {response}")
        data = None
        raise ValueError


    url_data = data['datos']

    api_call_data = ApiExtraction(
        url_data
    )

    headers_data = {
        "accept": "application/json"    
    }

    status, response = api_call_data.extract(
        method='get',
        headers= headers_data
    )

    print(response)



if __name__ == "__main__":
    main()