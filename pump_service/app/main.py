from typing import Union
import time, automationhat
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello From": "Pump Service"}

@app.get("/waternow")
def water_stable():
    print("Turning ON Pump")
    automationhat.relay.one.on()
    time.sleep(5)
    print("Turning OFF Pump")
    automationhat.relay.one.off()
    return {"status": "succes", "message": "plants watered for 5 sec"}

@app.get("/waterfor/{watering_duration}")
def water_for(watering_duration: int):
    print("Turning ON Pump")
    automationhat.relay.one.on()
    time.sleep(watering_duration)
    print("Turning OFF Pump")
    automationhat.relay.one.off()
    return {"status": "succes", "message": f"plants watered for {watering_duration} sec"}