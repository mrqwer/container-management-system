from sqlalchemy import select
from src.repositories.base_repository import BaseRepository
from src.models import Container


class ContainerRepository(BaseRepository):
    async def get_all(self):
        result = await self.db.execute(select(Container))
        return result.scalars().all()

    async def create(self, container_data: dict):
        container = Container(**container_data)
        self.db.add(container)
        await self.db.commit()
        await self.db.refresh(container)
        return container

    async def get_by_id(self, id: int):
        result = await self.db.execute(select(Container).where(Container.id == id))
        return result.scalar_one_or_none()

    async def update(self, container: Container):
        await self.db.commit()
        await self.db.refresh(container)
        return container
