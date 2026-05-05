from contextlib import asynccontextmanager # Imports a utility to create async lifecycle managers
from core.logger import logger
from core.scheduler import start_scheduler, stop_scheduler
from service.etf_service import ETFService
from providers.marketpriceprovider import MarketPriceProvider
from providers.inavpriceprovider import INavProvider
from db.session import Base, Engine
from fastapi import FastAPI
from routers import etftracking
from fastapi.responses import JSONResponse
from core.exceptions import AppException

@asynccontextmanager
async def lifespan(app: FastAPI): # defines app lifecycle manager
    # DB init
    Base.metadata.create_all(bind=Engine)

    # start scheduler
    start_scheduler()
    yield

    # shutdown
    stop_scheduler()

app = FastAPI(lifespan=lifespan) # attached life cycle logic

app.include_router(etftracking.router)

@app.exception_handler(AppException)
async def app_exception_handler(request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.message,
            "type": exc.__class__.__name__
        }
    )

@app.get("/etf_live_premium")
async def etf_premium():
    try:
        logger.info("Fetching live ETF premium")
        market_provider = MarketPriceProvider()
        inav_provider = INavProvider()
        etf = ETFService()
        return etf.calculate_premium(market_provider, inav_provider)

    except Exception as e:
        logger.error(f"Error fetching live premium: {e}")
        raise
