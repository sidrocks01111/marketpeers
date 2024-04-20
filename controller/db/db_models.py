"""DB Models"""
from typing import Optional
from beanie import Document

class ListedStocksIndia(Document):
    source: Optional[list[str]] = None
    exchange: str
    stock_name: Optional[str] = None
    stock_symbol: str
    stock_info: Optional[dict] = None
    stock_fin: Optional[dict] = None
    stock_profile: Optional[dict] = None
    
class allStocksSymbols(Document):
    symbol: str
    exchange: str
    exchangeShortName: str
    price: float
    name: str
    type: str
    