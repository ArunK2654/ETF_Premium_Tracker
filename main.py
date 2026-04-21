from service.etf_service import ETFService
from providers.marketpriceprovider import MarketPriceProvider
from providers.inavpriceprovider import INavProvider
from db.session import Base, Engine
from fastapi import FastAPI

app = FastAPI()

Base.metadata.create_all(bind=Engine)

@app.get("/etf_live_premium")
async def etf_premium():
    market_provider = MarketPriceProvider()
    inav_provider = INavProvider()

    etf = ETFService()
    return etf.calculate_premium(market_provider, inav_provider)





