from fastapi import APIRouter
from schemas.appointment import appointments, completed_appointments, cancelled_appointments


appointment_router = APIRouter()

@appointment_router.get("/")
def get_appointments():
    return {"Data": appointments}

@appointment_router.get("/completed/")
def get_completed_appointments():
    return {"Data": completed_appointments}

@appointment_router.get("/cancelled/")
def get_cancelled_appointments():
    return {"Data": cancelled_appointments}

