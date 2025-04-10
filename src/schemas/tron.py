from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TronAddressResponse(BaseModel):
    id: int
    address: str
    private_key: str
    created_at: Optional[datetime] = None

class TronRequest(BaseModel):
    address: str

class TronResponse(BaseModel):
    address: str
    balance: float
    bandwidth: int
    energy: int

class TronLogResponse(BaseModel):
    id: int
    address: str
    created_at: Optional[datetime] = None
