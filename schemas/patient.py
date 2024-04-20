from pydantic import BaseModel


class Patient(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: int
    height: int
    phone: str

class CreatePatient(BaseModel):
    name: str
    age: int
    sex: str
    weight: int
    height: int
    phone: str

class UpdatePatient(BaseModel):
    name: str
    weight: int
    height: int
    phone: str

patients: list[Patient] = [
    Patient(id=1,name="Sophia Johnson",age=23,sex="F",weight=34,height=192, phone="07046354236"),
    Patient(id=2,name="Ethan Martinez",age=32,sex="M",weight=34,height=192, phone="07046354245"),
    Patient(id=3,name="Olivia Brown",age=45,sex="F",weight=34,height=192, phone="07046353536"),
    Patient(id=4,name="Liam Anderson",age=63,sex="M",weight=34,height=192, phone="070463674236"),
    Patient(id=5,name="Emma Garcia",age=24,sex="F",weight=34,height=192, phone="07044554236"),
    Patient(id=6,name="Isabella Rodriguez",age=25,sex="MF",weight=34,height=192, phone="07046754236"),
    Patient(id=7,name="Elijah Lee",age=27,sex="M",weight=34,height=192, phone="07047854236"),
    Patient(id=8,name="Benjamin Smith",age=30,sex="M",weight=34,height=192, phone="07047854236")
]