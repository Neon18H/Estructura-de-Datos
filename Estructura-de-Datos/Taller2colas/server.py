# se debe instalar uvicorn: pip install uvicorn
# se debe instalar FastAPI: pip install fastapi
# se debe instalar pydantic: pip install pydantic
# COmando para ejecutar el servidor uvicorn server:app --reload --port 8080
from fastapi import FastAPI
from models.vehiclemanager import Vehiclemanager
from models import Vehicle

from classes import vehiclemanager as vm
from fastapi.responses import JSONResponse

from models import vehiclemanager as vm


app = FastAPI()
vehiclemanager = Vehiclemanager()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/register")
def register(vehicle: Vehicle):
    vm.add_vehicle(vehicle)
    return {"data": vehicle.dict()}

@app.get("/vehicles/pending")
def get_pending_vehicles():
    # Iterating directly to build the JSON response
    vehicles = []
    current = vm.first_pending
    while current:
        vehicles.append(current.value.dict())
        current = current.next
    return JSONResponse(content={"pending_vehicles": vehicles})

@app.get("/vehicles/tested")
def get_tested_vehicles():
    # Iterating directly to build the JSON response
    vehicles = []
    current = vm.first_tested
    while current:
        vehicles.append(current.value.dict())
        current = current.next
    return JSONResponse(content={"tested_vehicles": vehicles})

@app.post("/vehicles/execute-tests")
def execute_tests():
    vehicle = vm.execute_tests_for_vehicle()
    if vehicle:
        return {"vehicle": vehicle.dict(), "message": "Pruebas ejecutadas."}
    return {"message": "No hay vehículos pendientes para revisar."}

@app.delete("/vehicles/{tuition}/remove")
def remove_vehicle(tuition: str):
    vehicle_removed = vm.remove_pending_vehicle(tuition)
    if vehicle_removed:
        return {"message": "Vehículo retirado correctamente."}
    else:
        return {"message": "Vehículo no encontrado o ya no está pendiente."}

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

