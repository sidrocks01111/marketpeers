from typing import Optional
import requests
import json

from fastapi import APIRouter, HTTPException
from api_client.config import constants

async def get_request_url(_url: str, params: dict, backupPath: Optional[str] = None):
    """
    common function to make api calls using urls
    @_url: url requested
    @params: parameters
    @backupPath: backup path for the data
    """
    
    try:
        result = requests.get(_url, params=params)
        result = result.json()
        
        if backupPath:
            with open(backupPath, 'w') as file:
                json.dump(result, file, indent=3)
        
        return result
                
    except requests.exceptions.HTTPError as errh:
        raise HTTPException(status_code=500, detail=f"HTTP Error: {errh}")