from typing import Optional
from fastapi import APIRouter, Query
from api_client.db_connector import ListedStocksIndia, allStocksSymbols
from controller.api.web_endpoints.fmp import stocks_data

router = APIRouter()

@router.post("/get-nse-stocks-data/query")
async def get_stocks_data_query(
    query: Optional[dict] = None, 
    page_size: int = Query(default=10), 
    page: int = Query(default=1)
    )->dict:
    """
    api to get stocks data
    @query: query conditions to get results
    @page_size: limit the results
    @page: enter the page number
    """
    skip_count = (page - 1) * page_size
    stocks_results = []

    if query:
        stocks_results = {"entries": await ListedStocksIndia.find(query).skip(skip_count).limit(page_size).to_list()}
    else:
        stocks_results = {"entries": await ListedStocksIndia.find_all().skip(skip_count).limit(page_size).to_list()}
        
    stocks_results["total"] = len(stocks_results["entries"]) 
    return stocks_results

@router.post("/get-all-stocks-data/query")
async def get_all_stocks_data_query(
    query: Optional[dict] = None, 
    page_size: int = Query(default=10), 
    page: int = Query(default=1)
    )->dict:
    """
    api to get all stocks data
    @query: query conditions to get results
    @page_size: limit the results
    @page: enter the page number
    """
    skip_count = (page - 1) * page_size
    stocks_results = []
    if query == "all":
        stocks_results = {"entries": await allStocksSymbols.find(query).to_list()}
    elif query:
        stocks_results = {"entries": await allStocksSymbols.find(query).skip(skip_count).limit(page_size).to_list()}
    else:
        stocks_results = {"entries": await allStocksSymbols.find_all().skip(skip_count).limit(page_size).to_list()}
        
    stocks_results["total"] = len(stocks_results["entries"]) 
    return stocks_results

@router.get("/updatedb/web_endpoints")
async def updatedb_web_endpoints()->str:
    """
    function to update DB using web endpoints eg. FMP, ALPHA VANTAGE etc.
    """
    queryList = ["a", "b"]
    for item in queryList:
        await stocks_data.get_stock_info(query=item, exchange="NSE")
    await stocks_data.get_stock_fin(exchange="NSE")
    
    return "update stock data in DB"
