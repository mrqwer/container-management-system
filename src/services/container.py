from fastapi import HTTPException
from sqlalchemy.ext import AsyncSession
from src.services.base_service import BaseService
from src.schemas import ContainerCreate
from src.repositories import ContainerRepository


class ContainerService(BaseService):
    def __init__(self, db: AsyncSession):
        super().__init__(db)
        self.repo = ContainerRepository(db)

    async def create_container(self, schema: ContainerCreate):
        return await self.repo.create(schema.model_dump())

    async def list_containers(self):
        return await self.repo.get_all()

    async def update_container_status(self, container_id: int, status: str):
        container = await self.repo.get_by_id(container_id)
        if not container:
            raise HTTPException(status_code=404, detail="Container not found")

        container.status = status
        return await self.repo.update(container)

    async def get_by_id(self, container_id: int):
        return await self.repo.get_by_id(container_id)
