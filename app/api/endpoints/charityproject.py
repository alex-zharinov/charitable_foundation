from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (check_charityproject_exists,
                                check_name_duplicate)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charityproject import charityproject_crud
from app.models import Donation
from app.schemas.charityproject import (CharityProjectCreate, CharityProjectDB,
                                        CharityProjectUpdate)
from app.services.invest import (close_charity_project,
                                 invest_in_charity_project)

router = APIRouter()


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def create_new_charityproject(
        charityproject: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров."""
    await check_name_duplicate(charityproject.name, session)
    new_charityproject = await charityproject_crud.create(charityproject, session, comm=True)
    donations = await session.execute(
        select(Donation).where(Donation.fully_invested == 0)
    )
    donations = donations.scalars().all()
    await invest_in_charity_project(new_charityproject, donations)
    await session.commit()
    await session.refresh(new_charityproject)
    return new_charityproject


@router.patch(
    '/{charityproject_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def partially_update_charityproject(
        charityproject_id: int,
        obj_in: CharityProjectUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров."""
    charityproject = await check_charityproject_exists(
        charityproject_id, session
    )

    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, session)
    if obj_in.full_amount is not None and obj_in.full_amount < charityproject.invested_amount:
        raise HTTPException(
            status_code=400,
            detail='Сумма проекта меньше внесённой!',
        )
    if charityproject.fully_invested == 1:
        raise HTTPException(
            status_code=400,
            detail='Закрытый проект нельзя редактировать!',
        )
    charityproject = await charityproject_crud.update(
        charityproject, obj_in, session
    )
    if charityproject.full_amount == charityproject.invested_amount:
        await close_charity_project(charityproject, session)
        await session.refresh(charityproject)
    return charityproject


@router.get(
    '/',
    response_model=list[CharityProjectDB],
    response_model_exclude_none=True,
)
async def get_all_charityprojects(
        session: AsyncSession = Depends(get_async_session),
):
    all_rooms = await charityproject_crud.get_multi(session)
    return all_rooms


@router.delete(
    '/{charityproject_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def remove_meeting_room(
        charityproject_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    """Только для суперюзеров."""
    charityproject = await check_charityproject_exists(
        charityproject_id, session
    )
    if charityproject.invested_amount == 0 and not charityproject.fully_invested:
        charityproject = await charityproject_crud.remove(
            charityproject, session
        )
    else:
        raise HTTPException(
            status_code=400,
            detail='В проект были внесены средства, не подлежит удалению!',
        )
    return charityproject
