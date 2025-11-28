from fastapi import APIRouter

from src.controller.v1.zone import router as zone_router
from src.controller.v1.container import router as container_router

v1 = APIRouter(prefix="/v1")

v1.include_router(zone_router, prefix="/zone", tags=["zone"])
v1.include_router(container_router, prefix="/container", tags=["container"])