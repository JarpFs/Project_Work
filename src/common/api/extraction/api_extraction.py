import requests

#URL de la API pública (JSONPlaceholder)
url = 'https://jsonplaceholder.typicode.com/posts'

# Realizar una solicitud GET para obtener los datos
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta JSON a un diccionario de Python
    data = response.json()
    print(f"Datos recibidos: {data[:5]}")  # Imprimir los primeros 5 elementos
else:
    print(f"Error al hacer la solicitud. Código de estado: {response.status_code}")