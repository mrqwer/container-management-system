from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from typing import List
from src.schemas import ZoneRead
from src.database.connection import get_db
from src.services.management import WarehouseService

router = APIRouter()

@router.get("/zones", response_model=List[ZoneRead])
async def get_zones(db: AsyncSession = Depends(get_db)):
    svc = WarehouseService(db)
    return await svc.list_zones()


@router.post("/zones/{id}/assign")
async def assign_zone(id: int, container_id: int, db: AsyncSession = Depends(get_db)):
    svc = WarehouseService(db)
    return await svc.assign_container_to_zone(zone_id=id, container_id=container_id)


