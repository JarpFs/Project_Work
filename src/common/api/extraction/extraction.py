import requests

from common.logger.logger import get_logger

logger = get_logger(__name__)

class ApiExtraction():
    pass


def main() -> None:
    #URL de la API pública (JSONPlaceholder)
    url = 'https://jsonplaceholder.typicode.com/posts'

    # Realizar una solicitud GET para obtener los datos
    response = requests.get(url)

    # Verificar que la solicitud fue exitosa
    if response.status_code == 200:
        # Convertir la respuesta JSON a un diccionario de Python
        data = response.json()
        logger.info(f"Datos recibidos: {data[:5]}")  # Imprimir los primeros 5 elementos
    else:
        logger.error(f"Error al hacer la solicitud. Código de estado: {response.status_code}")

if __name__ == "__main__":
    main()