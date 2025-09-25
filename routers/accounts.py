# routers/accounts.py
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from models import Account
from schemas import AccountCreate
from database import fake_accounts_db
from auth import verify_token

router = APIRouter(prefix="/accounts", tags=["accounts"])

id_counter = 1

#@router.post("/", response_model=Account, status_code=201, dependencies=[Depends(verify_token)])
@router.post("/", response_model=Account, status_code=201)
def create_account(account: AccountCreate):
    global id_counter
    new_account = Account(id=id_counter, **account.dict())
    id_counter += 1
    fake_accounts_db.append(new_account)
    return new_account

#@router.get("/", response_model=List[Account], dependencies=[Depends(verify_token)])
@router.get("/", response_model=List[Account])
def get_accounts(skip: int = 0, limit: int = 10):
    return fake_accounts_db[skip:skip + limit]

#@router.get("/{account_id}", response_model=Account, dependencies=[Depends(verify_token)])
@router.get("/{account_id}", response_model=Account)
def get_account(account_id: int):
    for acc in fake_accounts_db:
        if acc.id == account_id:
            return acc
    raise HTTPException(status_code=404, detail="Account not found")
