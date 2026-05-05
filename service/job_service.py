from routers.etftracking import DBSession
from service.etf_service import ETFService
from repositories.etf_repository import ETFRepository
from providers.marketpriceprovider import MarketPriceProvider
from providers.inavpriceprovider import INavProvider
from core.logger import logger
from db.session import SessionLocal

async def run_etf_job():
    DBSession = SessionLocal()

    try:
        logger.info("ETF Job Started")

        # Fetch price
        market_provider = MarketPriceProvider()
        inav_provider = INavProvider()

        # create repo and service instance
        repo = ETFRepository(db=DBSession)
        etfservice = ETFService(repo)

        # calculate premium
        data = etfservice.calculate_premium(market_provider,inav_provider)

        # save to repository
        repo.save_etf(data.get("market_price"),data.get("inav_price"),data.get("percent"),data.get("status"))

        logger.info("ETF Job completed successfully.")

    except Exception as e:
        logger.error(f"Job Error: {e}")

    finally:
        DBSession.close()



