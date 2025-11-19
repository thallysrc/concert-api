from typing import List, Annotated

from fastapi import APIRouter, Depends

from app.api.schemas import Concert
from app.infrastructure.database.connection import get_db
from app.infrastructure.repositories.concert_repository import ConcertRepository
from app.application.services.concert_service import ConcertService

router = APIRouter(prefix="/concerts", tags=["Concerts"])

def get_concert_repository(db=Depends(get_db)):
    return ConcertRepository(db)

def get_concert_service(repo=Depends(get_concert_repository)):
    return ConcertService(repo)

ConcertServiceDp = Annotated[ConcertService, Depends(get_concert_service)]

@router.post("/", response_model=List[Concert])
async def create_concert(
    data: Concert,
    service: ConcertServiceDp,
):
    return await service.create(data)

