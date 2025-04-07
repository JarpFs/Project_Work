import logging


def get_logger(logger_name):
    """
    Función para obtener el logger de Spark con Log4j.
    
    Parámetros:
    - logger_name (str): Nombre del logger que se usará.

    Retorna:
    - log4j_logger: Un logger basado en Log4j si existe una sesión de Spark, de lo contrario un logger de Python.
    """
    try:
        from pyspark.sql import SparkSession

        # Intentar obtener la sesión de Spark existente
        spark = SparkSession.getActiveSession()
        
        if not spark:
            raise ValueError("No hay una sesión de Spark activa.")

        # Obtener el SparkContext y el logger de Log4j
        sc = spark.sparkContext
        log4j_logger = sc._jvm.org.apache.log4j.LogManager.getLogger(logger_name)
        log4j_logger.info("Initializated logger")
        return log4j_logger
    
    except Exception as e:
        # Si no se puede obtener la sesión de Spark o Log4j, retornar un logger de Python
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(logger_name)
        logger.warning(f"Logger Log4j no disponible, usando logger de Python: {e}")
        return logger