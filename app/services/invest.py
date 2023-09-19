from datetime import datetime

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.models import CharityProject, Donation


async def invest_in_charity_project(
        charityproject: CharityProject,
        donations: list[Donation]
) -> None:
    for donat in donations:
        if donat.full_amount - donat.invested_amount == charityproject.full_amount - charityproject.invested_amount:
            charityproject.fully_invested = True
            charityproject.invested_amount = charityproject.full_amount
            charityproject.close_date = datetime.now()
            donat.fully_invested = True
            donat.invested_amount = donat.full_amount
            donat.close_date = datetime.now()
            return
        if donat.full_amount - donat.invested_amount > charityproject.full_amount - charityproject.invested_amount:
            donat.invested_amount += charityproject.full_amount - charityproject.invested_amount
            charityproject.fully_invested = True
            charityproject.invested_amount = charityproject.full_amount
            charityproject.close_date = datetime.now()
            return
        if donat.full_amount - donat.invested_amount < charityproject.full_amount - charityproject.invested_amount:
            charityproject.invested_amount += donat.full_amount - donat.invested_amount
            donat.fully_invested = True
            donat.invested_amount = donat.full_amount
            donat.close_date = datetime.now()
    return


async def close_charity_project(
    charityproject: CharityProject,
    session: AsyncSession = Depends(get_async_session),
) -> None:
    charityproject.invested_amount = charityproject.full_amount
    charityproject.fully_invested = True
    charityproject.close_date = datetime.now()
    await session.commit()
    return


async def invest_new_donation(
        donation: Donation,
        charityprojects: list[CharityProject]
) -> None:
    for project in charityprojects:
        if project.full_amount - project.invested_amount == donation.full_amount - donation.invested_amount:
            donation.fully_invested = True
            donation.invested_amount = donation.full_amount
            donation.close_date = datetime.now()
            project.fully_invested = True
            project.invested_amount = project.full_amount
            project.close_date = datetime.now()
            return
        if project.full_amount - project.invested_amount > donation.full_amount - donation.invested_amount:
            project.invested_amount += donation.full_amount - donation.invested_amount
            donation.fully_invested = True
            donation.invested_amount = donation.full_amount
            donation.close_date = datetime.now()
            return
        if project.full_amount - project.invested_amount < donation.full_amount - donation.invested_amount:
            donation.invested_amount += project.full_amount - project.invested_amount
            project.fully_invested = True
            project.invested_amount = project.full_amount
            project.close_date = datetime.now()
    return
