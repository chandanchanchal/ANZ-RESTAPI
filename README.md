# FastAPI REST API Training

## Setup
1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
## Install dependencies:
  pip install -r requirements.txt
## Run API:
  uvicorn main:app --reload
##Access Swagger docs:
  http://127.0.0.1:8000/docs
