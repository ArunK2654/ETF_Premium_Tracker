from db.session import SessionLocal
from db.models import ETFPriceTracker
from core.logger import logger

class RepositoryService:
    def save_etf(self, market_price, inav_price, percent, status):

        # get db session
        db = SessionLocal()

        # fetch live data
        data = ETFPriceTracker(market_price=market_price, inav_price=inav_price, premium_percent=percent, status=status)

        # save the data in db
        db.add(data)
        db.commit()
        db.close()
        logger.info("Saved to Database")