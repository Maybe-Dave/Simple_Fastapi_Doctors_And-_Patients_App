from typing import Annotated

from fastapi import APIRouter, Depends

from schemas.patient import Patient,patients,CreatePatient,UpdatePatient
from schemas.appointment import Appointment, CreateAppiontment, appointments
from services.patient import patient_service
from services.appointment import appointment_service

patient_router = APIRouter()


@patient_router.get("/")
def get_patients():
    """
    Returns A list of all patients
    """
    return{"Message": "Data Retieved Successfully", "Data": patients }

@patient_router.get("/{pat_id}")
def get_patient_by_id(pat_id: Annotated[int, Depends(patient_service.patient_depends)]):
    """
    Returns A patient with recieved ID
    """
    data: Patient = patient_service.check_id(pat_id)
    return{"Message": "Data Retieved Successfully", "Data": data }

@patient_router.post("/", status_code=201)
def create_patient(payload: CreatePatient):
    """
    Creates A Patient
    """
    patient_service.create_patient(payload)
    return{"Message": "New Patient Created Successfully", "Data": patients }

@patient_router.put("/{pat_id}", status_code=200)
def update_patient_details( payload: UpdatePatient, pat_id: Annotated[int, Depends(patient_service.patient_depends)]):
    """
    Updates the details of a patient
    """
    data = patient_service.update_details(pat_id, payload=payload)
    return{"Message": "Patient Details Editted Successfully", "Data": data }

@patient_router.delete("/{pat_id}", status_code=200)
def delete_patient(pat_id: Annotated[int, Depends(patient_service.patient_depends)]):
    patient_service.delete_patient(pat_id)
    return{"Message": "Patient Deleted Succesfully", "Data": patients }

@patient_router.post("/appointments/{pat_id}")
def create_appointment(pat_id: Annotated[int, Depends(patient_service.patient_depends)]):
    data = patient_service.generate_appointment(pat_id)
    return {"Message":"Apppointment Created Successfully", "Data": data}

@patient_router.delete("/appointments/{pat_id}")
def complete_appointment(pat_id: Annotated[int, Depends(patient_service.patient_depends)]):
    patient_service.complete_appointment(pat_id)
    return {"Message":"Appointment completed Successfully ","Data": appointments}

@patient_router.delete("/appointments_cancel/{pat_id}")
def cancel_appointment(pat_id: Annotated[int,Depends(appointment_service.appointment_depends)] ):
   patient_service.cancel_appointment(pat_id)
   return {"Message":"Appointment Cancelled Successfully ","Data": appointments}