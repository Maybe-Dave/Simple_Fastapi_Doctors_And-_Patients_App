from pydantic import BaseModel

from schemas.patient import Patient
from schemas.doctor import Doctor

class Appointment(BaseModel):
    id: int
    patient: Patient
    doctor: Doctor
    date: str

class CreateAppiontment(BaseModel):
    date: str


appointments: list[Appointment] = [
    Appointment(id=1,
                patient=Patient(
                                id=1,
                                name="Sophia Johnson",
                                age=23,
                                sex="F",
                                weight=34,
                                height=192, 
                                phone="07046354236"),
                doctor=Doctor(
                                id=1,
                                specialization="Cardiology",phone="09078563428",
                                is_available=False),
                date="09-04-2023" ),

    Appointment(id=2,
                patient= Patient(
                                id=2,
                                name="Ethan Martinez",
                                age=32,
                                sex="M",
                                weight=34,
                                height=192, 
                                phone="07046354245"),

                doctor=Doctor(id=2,
                              specialization="Endocrinology",phone="07136472834",
                              is_available=False), 
                date="10-04-2023" )
]

completed_appointments: list[Appointment] = []
cancelled_appointments: list[Appointment] = []
