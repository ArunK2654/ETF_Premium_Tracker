from contextlib import asynccontextmanager # Imports a utility to create async lifecycle managers
from core.scheduler import start_scheduler, stop_scheduler
from service.etf_service import ETFService
from providers.marketpriceprovider import MarketPriceProvider
from providers.inavpriceprovider import INavProvider
from db.session import Base, Engine
from fastapi import FastAPI
from routers import etftracking

@asynccontextmanager
async def lifespan(app: FastAPI): # defines app lifecycle manager
    start_scheduler()
    yield
    stop_scheduler()

app = FastAPI(lifespan=lifespan) # attached life cycle logic

app.include_router(etftracking.router)

Base.metadata.create_all(bind=Engine)

@app.get("/etf_live_premium")
async def etf_premium():
    market_provider = MarketPriceProvider()
    inav_provider = INavProvider()
    etf = ETFService()
    return etf.calculate_premium(market_provider, inav_provider)





