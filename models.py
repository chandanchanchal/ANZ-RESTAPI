# models.py
from pydantic import BaseModel
from typing import Optional

class Account(BaseModel):
    id: int
    owner: str
    balance: float

class Transaction(BaseModel):
    id: int
    account_id: int
    type: str  # "credit" or "debit"
    amount: float

