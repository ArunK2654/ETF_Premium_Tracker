from service.etf_service import ETFService
from service.repository_service import RepositoryService
from providers.marketpriceprovider import MarketPriceProvider
from providers.inavpriceprovider import INavProvider
from core.logger import logger

async def run_etf_job():
    try:
        market_provider = MarketPriceProvider()
        inav_provider = INavProvider()
        etfservice = ETFService()
        repositoryservice = RepositoryService()

        data = etfservice.calculate_premium(market_provider,inav_provider)
        repositoryservice.save_etf(data.get("market_price"),data.get("inav_price"),data.get("percent"),data.get("status"))

    except Exception as e:
        logger.error(f"Job Error: {e}")



