from pydantic import BaseModel


class TronRequest(BaseModel):
    address: str

class TronResponse(BaseModel):
    address: str
    balance: float
    bandwidth: int
    energy: int
