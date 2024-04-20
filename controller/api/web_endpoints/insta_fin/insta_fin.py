# """API MODULE TO FETCH DATA FROM INSTA FINANCIALS""
import requests
import json

from fastapi import APIRouter
from api_client.config import constants

router = APIRouter()

@router.get("/demo-data")
async def get_data() -> list:
    """get data api"""
    url = "https://instafinancials.com/api/GetCIN/v1/json/Search/CBLDATA/Mode/SW"
    request_headers = { 'user-key': 'cTmC1lJcLVZ+FinR9AfYmgSbzMt/hljxNSvMUmOT3AxzjM7QWwphEA==' }
    response = requests.get(url, headers = request_headers)
    return response