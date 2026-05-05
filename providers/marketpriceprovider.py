import yfinance
from core.logger import logger
from core.exceptions import MarketDataError

class MarketPriceProvider:
    def get_market_price(self, etf_name="MON100.NS"):
        try:
            logger.info("Fetching market price")
            ticker = yfinance.Ticker(etf_name)
            market_price = round(ticker.info["currentPrice"],2)
            logger.debug(f"Market price fetched: {market_price}")
            return market_price

        except Exception as e:
            logger.error(f"Market price not fetched: {e}")
            raise MarketDataError(f"Failed to fetch market price: {str(e)}")