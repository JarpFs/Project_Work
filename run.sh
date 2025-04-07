#!/bin/bash

# Ruta absoluta al directorio del proyecto
PROJECT_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Ruta al directorio src
SRC_PATH="$PROJECT_ROOT/src"

# Agrega src al PYTHONPATH
export PYTHONPATH="$SRC_PATH:$PYTHONPATH"

# Verifica si se pasó un script
if [ -z "$1" ]; then
    echo "Por favor, pasa el nombre del script de Python que deseas ejecutar."
    echo "Uso: ./run.sh src/scripts/algo.py"
    exit 1
fi

# Verifica si el script existe
if [ -f "$1" ]; then
    echo "Ejecutando $1..."
    python "$1"
else
    echo "El archivo $1 no existe."
    exit 1
fi
