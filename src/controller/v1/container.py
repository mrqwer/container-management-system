from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from src.schemas import ContainerRead, ContainerCreate
from src.database.connection import get_db
from src.services.management import WarehouseService

router = APIRouter()

@router.get("/containers", response_model=List[ContainerRead])
async def get_containers(db: AsyncSession = Depends(get_db)):
    svc = WarehouseService(db)
    return await svc.list_containers()


@router.post("/containers", response_model=ContainerRead)
async def create_container(item: ContainerCreate, db: AsyncSession = Depends(get_db)):
    svc = WarehouseService(db)
    return await svc.create_container(item)


@router.patch("/containers/{id}")
async def update_status(id: int, status: str, db: AsyncSession = Depends(get_db)):
    svc = WarehouseService(db)
    return await svc.update_container_status(id, status)

