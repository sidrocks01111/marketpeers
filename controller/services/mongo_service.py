from typing import Optional
from fastapi import HTTPException
from pymongo import UpdateOne
from api_client.db_connector import ListedStocksIndia, db



class MongoService:
    
    @classmethod
    async def insert_to_listedStocksData(self, listed_stock_data: list):
        """
        function to insert or update data in listedStocksdata table
        @listed_stock_data: stocks data
        """
        try:
            bulk_operations = [
                UpdateOne(
                    {"stock_symbol": stock_data["set"]["stock_symbol"]},
                    {
                        "$set": stock_data["set"],
                        "$addToSet": stock_data["addToSet"]
                    },
                    upsert=True
                )
                for stock_data in listed_stock_data
            ]
            listed_stock_collection = db["ListedStocksIndia"]
            await listed_stock_collection.bulk_write(bulk_operations)
            
        except Exception as e:
            raise HTTPException(status_code=404, detail=str(e))
        
    
    @classmethod    
    async def insert_to_allStocksSymbols(self, all_stocks_list: list):
        """
        function to insert or update data in listedStocksdata table
        @all_stocks_list: stocks symbols data
        """
        try:
            bulk_operations = [
                UpdateOne(
                    {"symbol": stock_data["symbol"]},
                    {
                        "$set": stock_data
                    },
                    upsert=True
                )
                for stock_data in all_stocks_list
            ]
            all_stocks_collection = db["allStocksSymbols"]
            await all_stocks_collection.bulk_write(bulk_operations)
            
        except Exception as e:
            raise HTTPException(status_code=404, detail=f"error while insert in DB: {e}")
        
    
    @classmethod    
    async def get_listedStocksData_query(
        self,
        match_query: Optional[dict] = None, 
        fields_req: Optional[list] = None, 
        page: Optional[int] = None, 
        size: Optional[int] = None):
        """get function call to DB"""
        
        pipeline = []
        
        if match_query:
            pipeline.append({"$match": match_query})
        if fields_req:
            project_dict = {field: 1 for field in  fields_req}
            project_dict["_id"] = 0
            pipeline.append({"$project": project_dict})
        if page:
            pipeline.append({"$skip": (page - 1)*size})
        if size:
            pipeline.append({"$limit": size})
        
        print(pipeline)
        res = await ListedStocksIndia.aggregate(pipeline).to_list()
        return res