from fastapi.responses import HTMLResponse
from fastapi import FastAPI

#Crear una instancia de FastAPI
app = FastAPI()
app.title = 'Aplicacion de Ventas'
app.version = '0.0.1'

# Ventas
ventas = [
    {'id': 1, 'nombre': 'Laptop', 'precio': 1000},
    {'id': 2, 'nombre': 'Mouse', 'precio': 10},
    {'id': 3, 'nombre': 'Teclado', 'precio': 20},
]

# Crear punto de entreda
@app.get("/", tags=['Inicio'])  #Cavmio de etiqueta en Documentacion
def mensaje():
    return "Bienvenido, a FastAPI"

@app.get("/html", tags=["Inicio"])
def tags():
    return HTMLResponse(content="<h1> Bienvenido a FastAPI </h1>")

@app.get("/ventas", tags=['Ventas'])
def detalles_ventas():
    return ventas

@app.get("/ventas/{id}", tags=['Ventas'])
def venta_id(id: int):
    for venta in ventas:
        if venta['id'] == id:
            return venta
    return {'mensaje': 'Venta no encontrada'}

@app.get('/ventas/', tags=['Ventas'])
def producto(nombre: str):
    return [elem for elem in ventas if elem['nombre'] == nombre]











