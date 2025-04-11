from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.tron import Tron
from src.db.database import get_db
from src.schemas.tron import TronResponse, TronRequest
from src.services.tron import get_account_info
from sqlalchemy import select

router = APIRouter(tags=["Tron"])

@router.post("/tron/address", response_model=TronResponse)
async def check_address_data(data: TronRequest, db: AsyncSession = Depends(get_db)):
    try:
        info = get_account_info(data.address)
        stmt = select(Tron).filter(Tron.address == data.address)
        result = await db.execute(stmt)
        existing = result.scalar_one_or_none()

        if existing:
            existing.balance = info["balance"]
            existing.bandwidth = info["bandwidth"]
            existing.energy = info["energy"]
        else:
            existing = Tron(
                address=data.address,
                balance=info["balance"],
                bandwidth=info["bandwidth"],
                energy=info["energy"]
            )
            db.add(existing)

        await db.commit()
        await db.refresh(existing)

        return TronResponse(
            address=data.address,
            balance=info["balance"],
            bandwidth=info["bandwidth"],
            energy=info["energy"]
        )

    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Операция с кошельком не удалась: {str(e)}"
        )

@router.get("/tron/queries")
async def get_tron_queries(limit: int, offset: int, db: AsyncSession = Depends(get_db)):
    stmt = (
        select(Tron)
        .order_by(Tron.created_at)
        .offset(offset)
        .limit(limit)
    )

    result = await db.execute(stmt)
    queries = result.scalars().all()
    return queries
