from fastapi import APIRouter

from controller.api.web_endpoints.insta_fin import insta_fin
from controller.api.web_endpoints.alpha_vantage import alpha_vantage
from controller.api.web_endpoints.fmp import stocks_data
from controller.api.web_endpoints.nse_website import nse_web
from controller.api import db_ops

router = APIRouter()

router.include_router(db_ops.router, tags=["DB APIs"], prefix="/db_ops")
router.include_router(alpha_vantage.router, tags=["ALPHA VANTAGE"], prefix="/alpha_vantage")
router.include_router(stocks_data.router, tags=["Financial Model Prep"], prefix="/fmp")
router.include_router(insta_fin.router, tags=["INSTA FIN"], prefix="/insta_fin")
router.include_router(nse_web.router, tags=["NSE Data"], prefix="/nse")

