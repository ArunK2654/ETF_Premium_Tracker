from fastapi import APIRouter,Depends
from db.models import ETFPriceTracker
from db.session import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db = Annotated[Session, Depends(get_db)]


@router.get("/latest")
async def lastest(db:db):
    return db.query(ETFPriceTracker)\
        .order_by(ETFPriceTracker.datetime.desc())\
        .limit(1)\
        .all()


@router.get("/history")
async def history(db: db, limit = 50):
    return db.query(ETFPriceTracker)\
        .order_by(ETFPriceTracker.datetime.desc())\
        .limit(limit)\
        .all()




