# routers/transactions.py
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from models import Transaction
from schemas import TransactionCreate
from database import fake_transactions_db, fake_accounts_db
from auth import verify_token

router = APIRouter(prefix="/transactions", tags=["transactions"])

id_counter = 1

@router.post("/", response_model=Transaction, status_code=201, dependencies=[Depends(verify_token)])
def create_transaction(tx: TransactionCreate):
    global id_counter
    # Validate account exists
    if not any(acc.id == tx.account_id for acc in fake_accounts_db):
        raise HTTPException(status_code=404, detail="Account not found")
    new_tx = Transaction(id=id_counter, **tx.dict())
    id_counter += 1
    fake_transactions_db.append(new_tx)
    return new_tx

@router.get("/", response_model=List[Transaction], dependencies=[Depends(verify_token)])
def get_transactions(skip: int = 0, limit: int = 10):
    return fake_transactions_db[skip:skip + limit]

