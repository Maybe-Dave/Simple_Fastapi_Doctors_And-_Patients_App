from typing import Annotated

from fastapi import APIRouter,Depends


from schemas.doctor import Doctor,doctors,CreateDoctor,UpdateDoctor
from services.doctor import doctor_service

doctor_router = APIRouter()


@doctor_router.get("/", status_code=200)
def get_doctors():
    """
    Returns A list of all doctors
    """
    return{"Message": "Data Retieved Successfully", "Data": doctors }

@doctor_router.get("/{doc_id}", status_code=200)
def get_doctor_by_id(doc_id: Annotated[int, Depends(doctor_service.doctor_depends)]):
    """
    Returns A Doctor with recieved ID
    """
    data: Doctor = doctor_service.check_id(doc_id)
    return{"Message": "Data Retieved Successfully", "Data": data }

@doctor_router.post("/", status_code=201)
def create_doctor(payload: CreateDoctor):
    """
    Creates A Doctor
    """
    doctor_service.create_doctor(payload)
    return{"Message": "New Doctor Created Successfuly", "Data": doctors }

@doctor_router.put("/{doc_id}", status_code=200)
def update_doctor_details( payload: UpdateDoctor, doc_id: Annotated[int, Depends(doctor_service.doctor_depends)]):
    """
    Updates the details of a patient
    """
    data = doctor_service.update_details(doc_id=doc_id, payload=payload)
    return{"Message": "Doctor Details Editted Successful", "Data": data }

@doctor_router.delete("/{doc_id}", status_code=200)
def delete_doctor(doc_id: Annotated[int, Depends(doctor_service.doctor_depends)]):
    doctor_service.delete_doctor(doc_id)
    return{"Message": "Doctor deleted Succesfully", "Data": doctors }

@doctor_router.put("/status/{doc_id}")
def set_availablity_status(doc_id: Annotated[int, Depends(doctor_service.doctor_depends)]):
    data: Doctor = doctor_service.check_status(doc_id)
    return {"Message": "Status Set Successfully", "Data": data}