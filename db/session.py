from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase

# Create Engine
url = "sqlite:///./etf.db"
Engine = create_engine(url=url)

# Create Session
SessionLocal = Session(bind=Engine, autocommit=False)

Base = DeclarativeBase()