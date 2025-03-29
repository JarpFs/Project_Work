#!/bin/bash

# Verificar si Python está instalado
if ! command -v python &> /dev/null
then
    echo "Python no está instalado. Por favor, instálalo."
    exit 1
fi

# Comprobar si se pasó un nombre de script
if [ -z "$1" ]; then
    echo "Por favor, pasa el nombre del script de Python que deseas ejecutar."
    echo "Uso: ./run.sh script.py"
    exit 1
fi

# Verificar si el archivo del script existe
if [ -f "$1" ]; then
    echo "Ejecutando $1..."
    python "$1"
else
    echo "El archivo $1 no existe."
    exit 1
fi
