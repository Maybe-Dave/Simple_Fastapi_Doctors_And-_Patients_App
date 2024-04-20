from pydantic import BaseModel
from enum import Enum


class Doctor(BaseModel):

    id: int
    specialization: str
    phone: str
    is_available: bool = True


class CreateDoctor(BaseModel):
    specialization: str
    phone: str
    is_available: bool = True

class UpdateDoctor(BaseModel):
    specialization: str
    phone: str

doctors: list[Doctor] =[
    Doctor(id=1,specialization="Cardiology",phone="09078563428",is_available=False),
    Doctor(id=2,specialization="Endocrinology",phone="07136472834",is_available=False),
    Doctor(id=3,specialization="General",phone="08046384657"),
    Doctor(id=4,specialization="General",phone="0713642645"),
    Doctor(id=5,specialization="Endocrinology",phone="071648563956"),
    Doctor(id=6,specialization="Cardiology",phone="09056473956"),
    Doctor(id=7,specialization="General",phone="08164536475"),
    Doctor(id=8,specialization="General",phone="08046374658")
]