from fastapi import APIRouter, Depends, Query
from db.session import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from repositories.etf_repository import ETFRepository
from service.etf_service import ETFService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

DBSession = Annotated[Session, Depends(get_db)]


@router.get("/latest")
async def latest(db:DBSession):
    repo = ETFRepository(db)
    service = ETFService(repo)
    return service.get_latest()


@router.get("/history")
async def history(db: DBSession, limit: int = Query(50, le=100)):
    repo = ETFRepository(db)
    service = ETFService(repo)
    return service.get_history(limit)



