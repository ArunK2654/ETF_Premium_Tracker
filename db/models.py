from db.session import Base
from sqlalchemy import String, Float, Integer, DateTime, Column
from datetime import datetime

class ETFPriceTracker(Base):
    __tablename__="etf_price_tracker"

    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime, default=datetime.now, index=True)
    market_price = Column(Float)
    inav_price = Column(Float)
    premium_percent = Column(Float)
    status = Column(String(50))