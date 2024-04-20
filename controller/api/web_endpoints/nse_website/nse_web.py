import json
import requests
import pandas as pd
from typing import Literal
from fastapi import APIRouter, UploadFile
from io import StringIO

from controller.services.mongo_service import MongoService

router = APIRouter()

Indexes = Literal[
    "NIFTY50",
    "NIFTY100",
    "NIFTY200"
]


@router.post("/nse/index_data/fileUpload")
async def uploadIndexData(file: UploadFile, index: Indexes):
    """
    function accepting csv files with index companies data
    Args:
       file: csv file with index data
    """

    file_content = await file.read()
    csv_content = file_content.decode("utf-8")
    csv_df = pd.read_csv(StringIO(csv_content),
                         header="infer", low_memory=False)
    json_data = csv_df.to_json(orient="records")
    data = json.loads(json_data)

    listed_stock_data = []

    for item in data:
        listed_stock_data.append({
            "set": {
                "source": ["NSE"],
                "stock_name": item["Company Name"],
                "stock_symbol": item["Symbol"],
                "stock_info.series": "EQ",
                "stock_info.isin_code": item["ISIN Code"],
                "stock_info.industry": item["Industry"]
            },
            "addToSet": {
                "stock_info.index": index,
            }
        })
    await MongoService.insert_to_listedStocksData(listed_stock_data=listed_stock_data)
    return listed_stock_data
