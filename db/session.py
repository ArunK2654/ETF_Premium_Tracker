from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# create Engine
url = "sqlite:///./etf.db"
Engine = create_engine(url=url)

# create Session
SessionLocal = sessionmaker(bind=Engine, autocommit=False)

# create Base
Base = declarative_base()