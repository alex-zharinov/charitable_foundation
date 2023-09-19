from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):
    async def get_charityproject_id_by_name(
            self,
            charityproject_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_charityproject_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == charityproject_name
            )
        )
        db_charityproject_id = db_charityproject_id.scalars().first()
        return db_charityproject_id

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ):
        projects = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested == 1
            )
        )
        return sorted(
            projects.scalars().all(),
            key=lambda obj: obj.close_date - obj.create_date
        )


charityproject_crud = CRUDCharityProject(CharityProject)
