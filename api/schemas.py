from pydantic import BaseModel


class MedicalBusinessBase(BaseModel):
    name: str
    description: str


class MedicalBusinessCreate(MedicalBusinessBase):
    pass


class MedicalBusiness(MedicalBusinessBase):
    id: int

    class Config:
        orm_mode = True
