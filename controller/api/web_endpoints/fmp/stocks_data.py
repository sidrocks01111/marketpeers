import time
from typing import Optional
import requests
import json

from fastapi import APIRouter, HTTPException
from api_client.config import constants
from controller.db.db_models import ListedStocksIndia
from controller.services.mongo_service import MongoService
from controller.api.common_api import url_requests


router = APIRouter()


@router.get("/get-all-stock-symbol")
async def get_all_stocks_symbols(fmp_api_key_user: Optional[str] = None):
    """
    function to get all stocks symbols
    """
    if fmp_api_key_user:
        fmp_api_key = fmp_api_key_user
    else:
        fmp_api_key = constants.FMP_API_KEY

    _url = "https://financialmodelingprep.com/api/v3/stock/list"

    params = {
        'apikey': fmp_api_key
    }

    result = await url_requests.get_request_url(_url, params, backupPath='.backup/all_stocks_etf_data.json')
    await MongoService.insert_to_allStocksSymbols(result)
    return len(result)


@router.get("/get-stock-info")
async def get_stock_info(exchange: str, fmp_api_key_user: Optional[str] = None):
    """get data api"""
    if fmp_api_key_user:
        fmp_api_key = fmp_api_key_user
    else:
        fmp_api_key = constants.FMP_API_KEY

    _url = "https://financialmodelingprep.com/api/v3/search"

    for char_code in range(ord('a'), ord('z')+1):
        print(chr(char_code))

        params = {
            'query': chr(char_code),
            'apikey': fmp_api_key,
            'exchange': exchange
        }
        result = await url_requests.get_request_url(_url, params, backupPath='.backup/data_stock_info.json')

        listed_stock_data = []
        for item in result:
            listed_stock_data.append(
                {"set": {
                    "source": ["FMP"],
                    "exchange": exchange,
                    "stock_name": item["name"],
                    "stock_symbol": editSymbolName(item["symbol"]),
                    "stock_info.currency": item["currency"],
                    "stock_info.stockExchange": item["stockExchange"]
                },
                "addToSet": {}})

        await MongoService.insert_to_listedStocksData(listed_stock_data)
    return "Inserted Stocks Data in DB"


@router.get("/get-stock-fin")
async def get_stock_fin(exchange: str, fmp_api_key_user: Optional[str] = None):
    """get data api"""
    if fmp_api_key_user:
        fmp_api_key = fmp_api_key_user
    else:
        fmp_api_key = constants.FMP_API_KEY

    _url = f"https://financialmodelingprep.com/api/v3/symbol/{exchange}"

    params = {
        'apikey': fmp_api_key
    }

    result = await url_requests.get_request_url(_url, params, backupPath='.backup/data_stock_fin.json')

    listed_stock_data = [

        {"set": {
            "source": ["FMP"],
            "exchange": exchange,
            "stock_symbol": editSymbolName(item['symbol']),
            "stock_fin": item
        },
        "addToSet": {}
}
        for item in result
    ]
    await MongoService.insert_to_listedStocksData(listed_stock_data)
    return listed_stock_data


@router.get("/get-stock-profile")
async def get_stock_profile(stock_symbol: str, fmp_api_key_user: Optional[str] = None):
    """
    get stock profile
    paid version for other than US stocks
    """

    if fmp_api_key_user:
        fmp_api_key = fmp_api_key_user
    else:
        fmp_api_key = constants.FMP_API_KEY

    params = {
        'apikey': fmp_api_key
    }

    stock_symbols_list = []

    if stock_symbol == 'all':
        stock_symbols_list = await MongoService.get_listedStocksData_query(fields_req=["stock_symbol"])
    else:
        stock_symbols_list = [stock_symbol]

    result_list = []

    for item in stock_symbols_list:
        item_symbol = item["stock_symbol"]
        _url = f"https://financialmodelingprep.com/api/v3/profile/{item_symbol}"
        result = await url_requests.get_request_url(_url, params, backupPath='.backup/data_stock_fin.json')
        result_list.append(result)

        with open('.backup/data_stocks_profile.json', 'w') as file:
            json.dump(result, file, indent=3)

    listed_stock_data = [

        {
            "set": 
            {
            "source": ["FMP"],
            "stock_symbol": editSymbolName(item['symbol']),
            "stock_profile": item
            },
            "addToSet": {}
        }

        for item in result_list
    ]
    await MongoService.insert_to_listedStocksData(listed_stock_data)

    return result_list

# utility function


def editSymbolName(stock_symbol: str) -> str:
    """
    function to edit symbol name
    """
    stock_symbol_new = stock_symbol
    stock_symbol_new = stock_symbol_new.split('.')
    stock_symbol_new = stock_symbol_new[0]

    return stock_symbol_new
