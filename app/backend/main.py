# -*- coding: utf-8 -*-
from fastapi import FastAPI, Depends
from backend import routers
from datetime import datetime
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("Running default data version scripts")

app.include_router(routers.router, prefix="/user", tags=['user'])