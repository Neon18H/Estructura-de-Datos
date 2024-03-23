# se debe instalar uvicorn: pip install uvicorn
# se debe instalar FastAPI: pip install fastapi
# se debe instalar pydantic: pip install pydantic
# COmando para ejecutar el servidor uvicorn server:app --reload --port 8080
from fastapi import FastAPI
from models.vehiclemanager import Vehiclemanager
from models import Vehicle

app = FastAPI()
vehiclemanager = Vehiclemanager()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/estado")
def estado():
    elementos = vehiclemanager.contar()
    return {"status": "ok", "elementos": elementos}

@app.post("/encolar")
def encolar(vehiculo: Vehicle):
    vehiclemanager.encolar(vehiculo)
    return {"status": "ok"}

@app.get("/desencolar")
def desencolar():
    elemento = vehiclemanager.desencolar()
    return {"status": "ok", "elemento": elemento}

@app.get("/ver_todos")
def ver_todos():
    elementos = vehiclemanager.ver_listado()
    return {"status": "ok", "elementos": elementos}