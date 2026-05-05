from core.exceptions import NavDataError, MarketDataError
from core.logger import logger
from repositories.etf_repository import ETFRepository

class ETFService:
    def __init__(self, repo=None):
        self.repo = repo

    def calculate_premium(self, market_provider, inav_provider):
        try:
            # fetch live prices
            market_price = market_provider.get_market_price()
            inav_price = inav_provider.get_inav_price()

            # validation
            if market_price is None:
                raise MarketDataError("Market price is missing")
            if inav_price is None:
                raise NavDataError("INav price is missing")
            if inav_price == 0:
                raise NavDataError("INav price cannot be zero")

            # compute premium
            logger.info("Calculating Premium")
            premium_percent = round(((market_price-inav_price)/inav_price * 100),2)
            logger.info(f"Premium percent is {premium_percent}%")

            if market_price > inav_price:
                status = "Premium"
            elif market_price < inav_price:
                status = "Discount"
            else:
                status = "At Par"

            return {
                    "market_price": market_price,
                    "inav_price": inav_price,
                    "percent": abs(premium_percent),
                    "status": status
                    }

        except (MarketDataError, NavDataError):
            raise

        except Exception as e:
            logger.error(f"Error calculating premium: {e}")
            raise MarketDataError("Unexpected error during premium calculation")


    def get_latest(self):
        logger.info("Fetching latest ETF data from repository")
        return self.repo.get_latest()

    def get_history(self, limit):
        logger.info("Fetching history ETF data from repository")
        return self.repo.get_history(limit)


