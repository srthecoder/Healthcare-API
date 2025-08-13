# This is the main file to load the GraphQL application as well as FastAPI.

from fastapi import FastAPI
from typing import List
from . import schema
from fastapi.responses import RedirectResponse
from .endpoints import Patients, Appointments, MedicalRecords, Medications 

app = FastAPI()
@app.get("/")
async def docs_redirect():
    response = RedirectResponse(url='/docs')
    return response