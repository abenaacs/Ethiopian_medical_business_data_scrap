from sqlalchemy.orm import Session
from . import models, schemas


def get_medical_business(db: Session, business_id: int):
    return (
        db.query(models.MedicalBusiness)
        .filter(models.MedicalBusiness.id == business_id)
        .first()
    )


def create_medical_business(db: Session, business: schemas.MedicalBusinessCreate):
    db_business = models.MedicalBusiness(**business.dict())
    db.add(db_business)
    db.commit()
    db.refresh(db_business)
    return db_business
