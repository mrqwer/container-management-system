from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from typing import List
import models, schemas, service


app = FastAPI(title="Warehouse API", version="1.0.0")


@app.get("/containers", response_model=List[ContainerRead])
async def get_containers(db: AsyncSession = Depends(get_db)):
    svc = service.WarehouseService(db)
    return await svc.list_containers()


@app.post("/containers", response_model=ContainerRead)
async def create_container(item: ContainerCreate, db: AsyncSession = Depends(get_db)):
    svc = service.WarehouseService(db)
    return await svc.create_container(item)


@app.patch("/containers/{id}")
async def update_status(id: int, status: str, db: AsyncSession = Depends(get_db)):
    svc = service.WarehouseService(db)
    return await svc.update_container_status(id, status)


@app.get("/zones", response_model=List[schemas.ZoneRead])
async def get_zones(db: AsyncSession = Depends(get_db)):
    svc = service.WarehouseService(db)
    return await svc.list_zones()


@app.post("/zones/{id}/assign")
async def assign_zone(id: int, container_id: int, db: AsyncSession = Depends(get_db)):
    svc = service.WarehouseService(db)
    return await svc.assign_container_to_zone(zone_id=id, container_id=container_id)


# --- Startup (Create Tables) ---
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
