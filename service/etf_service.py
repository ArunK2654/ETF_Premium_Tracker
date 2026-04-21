class ETFService:
    def calculate_premium(self, market_provider, inav_provider):
        self.market_provider = market_provider
        self.inav_provider = inav_provider

        market_price = self.market_provider.get_market_price()
        inav_price = self.inav_provider.get_inav_price()

        premium_percent = ((market_price-inav_price)/inav_price * 100)
        return {
                "market_price": market_price,
                "inav_price": inav_price,
                "percent": f"{abs(round(premium_percent,2))} %",
                "status": "Premium" if market_price>inav_price else "Discount"
            }
