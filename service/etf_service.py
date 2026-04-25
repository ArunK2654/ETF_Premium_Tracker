from core.logger import logger

class ETFService:
    def calculate_premium(self, market_provider, inav_provider):
        self.market_provider = market_provider
        self.inav_provider = inav_provider

        # fetch live prices
        market_price = self.market_provider.get_market_price()
        inav_price = self.inav_provider.get_inav_price()

        # compute premium
        logger.info("Calculating Premium...")
        premium_percent = round(((market_price-inav_price)/inav_price * 100),2)
        logger.info(f"Premium percent is {premium_percent}%")
        return {
                "market_price": market_price,
                "inav_price": inav_price,
                "percent": abs(premium_percent),
                "status": "Premium" if market_price>inav_price else "Discount"
                }
