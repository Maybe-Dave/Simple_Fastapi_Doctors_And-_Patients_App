from fastapi import HTTPException
from schemas.doctor import doctors,UpdateDoctor, Doctor,CreateDoctor

class DoctorService():

    @staticmethod
    def doctor_depends(doc_id:int):
        for doctor in doctors:
             if doctor.id == doc_id:
                 return doc_id
        raise HTTPException(status_code=404, detail="Doctor not found")
    
    @staticmethod
    def check_id(doc_id:int):
        for doc in doctors:
            if doc.id == doc_id:
                return doc
        raise HTTPException(status_code=404, detail="Doctor not found")

    @staticmethod
    def create_doctor(payload: CreateDoctor) ->None:
        new_id: int = len(doctors) + 1
        for doc in doctors:
            if doc.id == new_id:
                new_id += 1
        new_doctor = Doctor(
                id = doctor_service.check_id(new_id),
                specialization=payload.specialization,
                phone=payload.phone,
            )
        doctors.append(new_doctor)


    @staticmethod
    def update_details(doc_id:int, payload: UpdateDoctor) -> Doctor:
        current_doctor = None
        for doctor in doctors:
            if doctor.id == doc_id:
               current_doctor = doctor 
               break 
        if not current_doctor:
            raise HTTPException(status_code=404, detail="Doctor not found")
        current_doctor.phone = payload.phone or current_doctor.phone
        current_doctor.specialization = payload.specialization or current_doctor.specialization
        return current_doctor
    
    @staticmethod
    def delete_doctor(doc_id: int):
        for doc in doctors:
            if doc.id == doc_id:
                doctors.remove(doc)

    @staticmethod
    def check_status(doc_id:int):
        for doctor in doctors:
            if doctor.id == doc_id:
                if doctor.is_available == True:
                    doctor.is_available = False
                return doctor

        

    
doctor_service = DoctorService()
