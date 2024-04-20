# """API MODULE TO FETCH DATA FROM ALPHA VANTAGE"""
import requests
import json

from fastapi import APIRouter
from api_client.config import constants

router = APIRouter()

@router.get("/demo-data")
async def get_data() -> list:
    """get data api"""
    alpha_vantage_api_key = constants.ALPHA_VANTAGE_KEY
    _url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol=AAPL&apikey={alpha_vantage_api_key}"
    # _url = "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=tatamotors&apikey=PAC5Q4IEYJO9GV1X"
    response = requests.get(_url)
    result = response.json()
    with open('data.json', 'w') as file:
        json.dump(result, file, indent=3)
    return response