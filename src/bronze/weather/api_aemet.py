
from common.logger.logger import get_logger
from common.extract.base_extractors import ApiExtraction
import os
from dotenv import load_dotenv
import pandas as pd


load_dotenv()

logger = get_logger(__name__)
    


def main() -> None:

    api_key = os.getenv('KEY_AEMET')

    #URL Aemet public
    url = 'https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/estaciones/C419X'

    #Headers
    headers = {
        "accept": "application/json",
        "api_key": api_key
    }

    #API call with endpoint
    api_call = ApiExtraction(
        url
    )

    #Extract information 
    status, response = api_call.extract(
        method='get',
        headers = headers
    )

    #Obtain data information  from another url
    url_data = response['datos']

    api_call_data = ApiExtraction(
        url_data
    )

    try:
        logger.info(f"Complete extract data AEMET API from:{url_data}")
        status, data = api_call_data.extract(
        ) 
    except:
        data = None
        raise Exception


    print(data)



if __name__ == "__main__":
    main()