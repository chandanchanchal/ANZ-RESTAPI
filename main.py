# main.py
from fastapi import FastAPI, Request
from routers import accounts, transactions
import logging
from auth import router as auth_router

app = FastAPI(title="Banking REST API", version="1.0")


# Logging middleware
logging.basicConfig(level=logging.INFO)
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logging.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logging.info(f"Response Status: {response.status_code}")
    return response

# Include routers
app.include_router(accounts.router)
app.include_router(transactions.router)
app.include_router(auth_router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Banking REST API"}
