from fastapi import FastAPI
from app.models import engine, Base

app = FastAPI(title="AI Search Agent")

@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)