from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/businesses/", response_model=schemas.MedicalBusiness)
def create_business(
    business: schemas.MedicalBusinessCreate, db: Session = Depends(get_db)
):
    return crud.create_medical_business(db=db, business=business)


@app.get("/businesses/{business_id}", response_model=schemas.MedicalBusiness)
def read_business(business_id: int, db: Session = Depends(get_db)):
    return crud.get_medical_business(db=db, business_id=business_id)
