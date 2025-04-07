
from common.logger.logger import get_logger
from common.extract.base_extractors import ApiExtraction

logger = get_logger(__name__)


def main() -> None:

    #URL de la API pública (JSONPlaceholder)
    url = 'https://jsonplaceholder.typicode.com/posts'

    api_call = ApiExtraction(url)

    status, response = api_call.extract()

    # Verificar que la solicitud fue exitosa
    if status == 200:
        # Convertir la respuesta JSON a un diccionario de Python
        data = response.json()
        logger.info(f"Datos recibidos: {data[:5]}")  # Imprimir los primeros 5 elementos
    else:
        logger.error(f"Error al hacer la solicitud. Código de estado: {response.status_code}")

if __name__ == "__main__":
    main()