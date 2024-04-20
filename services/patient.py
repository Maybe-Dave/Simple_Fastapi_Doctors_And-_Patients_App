from datetime import datetime
from fastapi import HTTPException
from schemas.patient import patients,Patient,UpdatePatient,CreatePatient
from schemas.appointment import appointments,Appointment, completed_appointments, cancelled_appointments
from schemas.doctor import doctors, Doctor

class PatientService():

    @staticmethod
    def patient_depends(pat_id:int):
        for patient in patients:
             if patient.id == pat_id:
                 return pat_id
        raise HTTPException(status_code=404, detail="Patient not found")
    
    @staticmethod
    def check_id(pat_id:int) -> Patient:
        for pat in patients:
            if pat.id == pat_id:
                return pat
        raise HTTPException(status_code=404, detail="Patient not found")

    @staticmethod
    def create_patient(payload: CreatePatient) -> None:
        new_id:int = len(patients) + 1
        for pat in patients:
            if pat.id == new_id:
                new_id += 1
        new_patient = Patient(
            id=patient_service.check_id(new_id),
            name = payload.name,
            age = payload.age,
            sex=payload.sex,
            weight=payload.weight,
            height=payload.height,
            phone= payload.phone
        )
        patients.append(new_patient)
        


    @staticmethod
    def update_details(pat_id:int, payload: UpdatePatient) -> Patient:
        current_patient = None
        for patient in patients:
            if patient.id == pat_id:
                current_patient = patient
        current_patient.name = payload.name or current_patient.name
        current_patient.height = payload.height or current_patient.height
        current_patient.weight = payload.weight or current_patient.weight
        current_patient.phone = payload.phone or current_patient.phone
        return current_patient
    
    @staticmethod
    def delete_patient(pat_id:int) -> None:
        for pat in patients:
            if pat.id == pat_id:
                patients.remove(pat)


    @staticmethod
    def generate_appointment(pat_id:int):
        available_doctor: Doctor = None
        patient = None
        for pat in patients:
            if pat.id == pat_id:
                patient = pat
        for appointment in appointments:
            if appointment.patient.id == patient.id:
                raise HTTPException(status_code=408, detail="Patient is in an uncompleted appointment. Complete unfinished appointment to create anew appointment")
        for doctor in doctors:
            if doctor.is_available is True:
                available_doctor = doctor
                break
        if not available_doctor:
            raise HTTPException(status_code=503, detail="No Doctor is available at the moment")
        available_doctor.is_available = False
        new_appointment = Appointment(
                                id=len(appointments) +1,
                                doctor=available_doctor,
                                patient=patient,date=patient_service.get_date()
                                )
        appointments.append(new_appointment)
        return new_appointment

    @staticmethod
    def complete_appointment(pat_id: int):
        exist = False
        for appointment in appointments:
            if appointment.patient.id == pat_id:
                exist = True
                appointment.doctor.is_available = True
                completed_appointments.append(appointment)
                appointments.remove(appointment)
                break
        if not exist:
           raise HTTPException(status_code=404, detail="Patient does not have an appointment")
        

    @staticmethod
    def cancel_appointment(pat_id:int):
        exist = False
        for appointment in appointments:
            if appointment.patient.id == pat_id:
                exist = True
                appointment.doctor.is_available = True
                cancelled_appointments.append(appointment)
                appointments.remove(appointment)
                break
        if not exist:
            raise HTTPException(status_code=404, detail="Patient does not have an appointment")
        


    @staticmethod
    def get_date() -> str:
        today_date = datetime.today()
        formatted_date = today_date.strftime("%d-%m-%y")
        return formatted_date
            


patient_service = PatientService()
