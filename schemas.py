# schemas.py
from pydantic import BaseModel

class AccountCreate(BaseModel):
    owner: str
    balance: float

class TransactionCreate(BaseModel):
    account_id: int
    type: str
    amount: float

