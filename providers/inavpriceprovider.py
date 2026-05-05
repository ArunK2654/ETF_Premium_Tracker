import requests
from core.logger import logger
from core.exceptions import NavDataError


class INavProvider:
    def get_inav_price(self, etf_name="Motilal Oswal Nasdaq 100 ETF (MOFN100)"):
        url = "https://www.amfiindia.com/spages/NAVAll.txt"
        headers = {
            "Content-Type": "text/plain",
            "User-Agent": "Mozilla/5.0"
        }

        logger.info("Fetching INav price")
        try:
            response = requests.get(url= url, headers= headers, timeout=5)
        except requests.RequestException as e:
            logger.error(f"INav API request failed: {e}")
            raise NavDataError("INav API unreachable")

        if response.status_code != 200:
            logger.error(f"AmfiIndia Website returned StatusCode: {response.status_code}")
            raise NavDataError("Failed to fetch Nav details")

        result = response.text.split("\n")

        inav_price = None

        for row in result:
            data = row.split(";")
            if len(data) > 5:
                if data[3] == etf_name:
                    try:
                        inav_price = round(float(data[4]),2)

                    except ValueError:
                        logger.error(f"Invalid INav value: {data[4]}")
                        raise NavDataError("Invalid INav data format")

                    logger.debug(f"Inav price fetched: {inav_price}")
                    break

        if inav_price is None:
            logger.error(f"INav price not available")
            raise NavDataError("INav price not available")


        return inav_price