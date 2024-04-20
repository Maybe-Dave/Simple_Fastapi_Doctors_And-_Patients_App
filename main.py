from fastapi import FastAPI
from routers.doctor import doctor_router
from routers.patient import patient_router
from routers.appointment import appointment_router

app = FastAPI()

app.include_router(router=doctor_router,prefix="/doctors",tags=["DOCTOR"])
# Target the doctor or patient directly instead of using list indexing
app.include_router(router=patient_router,prefix="/patients",tags=["PATIENT"])
app.include_router(router=appointment_router,prefix="/appointments",tags=["APPOINTMENT"])

@app.get("/",tags=["Home Page"])
def home_page():
    return {"Message": "Welcome to Davix Hospital, where compassionate care meets cutting-edge innovation. Step into a world of healing and hope, where every heartbeat matters. Discover our commitment to excellence in healthcare as we pave the way towards a healthier tomorrow. Your journey to wellness begins here "}