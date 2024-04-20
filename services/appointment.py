from fastapi import HTTPException

from schemas.appointment import appointments

class AppointmentService():

    @staticmethod
    def appointment_depends(apo_id:int):
        for appointment in appointments:
            if appointment.id == apo_id:
                return apo_id
        raise HTTPException(status_code=404, detail="Apointment Not found")




appointment_service = AppointmentService()