from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base
from routers import search,recepies

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(search.router)
app.include_router(recepies.router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

