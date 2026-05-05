from core.logger import logger
from core.exceptions import MarketDataError
from db.models import ETFPriceTracker


class ETFRepository:
    def __init__(self, db: Session):
        self.db = db

    def save_etf(self, market_price, inav_price, percent, status):
        try:
            # fetch live data
            data = ETFPriceTracker(market_price=market_price, inav_price=inav_price, premium_percent=percent, status=status)

            # save the data in db
            self.db.add(data)
            self.db.commit()

            return data

        except Exception as e:
            self.db.rollback()
            raise


    def get_latest(self):
        try:
            return self.db.query(ETFPriceTracker) \
                .order_by(ETFPriceTracker.datetime.desc()) \
                .limit(1) \
                .first()
        except Exception as e:
            logger.error(f"Error fetching latest ETF data: {e}")
            raise MarketDataError("Database error while fetching latest data")

    def get_history(self, limit: int):
        try:
            return self.db.query(ETFPriceTracker) \
                .order_by(ETFPriceTracker.datetime.desc()) \
                .limit(limit) \
                .all()

        except Exception as e:
            logger.error(f"Error fetching ETF history: {e}")
            raise MarketDataError("Database error while fetching history")