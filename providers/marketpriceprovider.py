import yfinance
from core.logger import logger

class MarketPriceProvider:
    def get_market_price(self, etf_name="MON100.NS"):
        try:
            ticker = yfinance.Ticker(etf_name)
            market_price = ticker.info["currentPrice"]
            logger.info(f"Market price fetched: {market_price}")
            return market_price
        except:
            logger.error("Market price not fetched")