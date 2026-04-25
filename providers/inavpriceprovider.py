import requests
from core.logger import logger
from core.exceptions import NavDataError


class INavProvider:
    def get_inav_price(self):
        url = "https://www.amfiindia.com/spages/NAVAll.txt"
        headers = {
            "Content-Type": "text/plain",
            "User-Agent": "Mozilla/5.0"
        }

        logger.info("Fetching INav price...")
        response = requests.get(url= url, headers= headers)

        if response.status_code != 200:
            logger.error(f"AmfiIndia Website returned StatusCode: {response.status_code}")
            raise NavDataError("Failed to fetch Nav details")

        result = response.text.split("\n")

        inav_price = None

        for row in result:
            data = row.split(";")
            if len(data) > 5:
                if data[3] == "Motilal Oswal Nasdaq 100 ETF (MOFN100)":
                    inav_price = round(float(data[4]),2)
                    logger.debug(f"Inav price fetched: {inav_price}")

        if inav_price == None:
            logger.error(f"INav price not available")
            raise NavDataError("INav price not available")


        return inav_price