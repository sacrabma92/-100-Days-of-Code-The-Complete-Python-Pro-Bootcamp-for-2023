from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional, List

#Crear una instancia de FastAPI
app = FastAPI()
app.title = 'Aplicacion de Ventas'
app.version = '0.0.1'

# Ventas
ventas = [
    {'id': 1, 'nombre': 'Laptop', 'fecha': '31/01/2024', "tienda": 'TIENDA01', 'precio': 1000},
    {'id': 2, 'nombre': 'Mouse', 'fecha': '06/02/2024', "tienda": 'TIENDA02', 'precio': 10},
    {'id': 3, 'nombre': 'Teclado', 'fecha': '11/03/2024', "tienda": 'TIENDA03', 'precio': 20},
]

# Creacion de Modelo
class Ventas(BaseModel):
    id: Optional[int] = None
    nombre: str
    fecha: str
    tienda: str
    precio: float

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

#Agregamos una nueva venta con el metodo POST y por medio de Body() toca importarla
@app.post('/ventas', tags=['Ventas'])
def agregar_venta(venta: Ventas):
  ventas.append(venta)
  return {'mensaje': 'Venta agregada correctamente'}
    
@app.put('/ventas/{id}', tags=['Ventas'])
def actualizar_venta(id: int, venta: Ventas):
    for element in ventas:
        if element['id'] == id:
            element['nombre'] = venta.nombre
            element['fecha'] = venta.fecha
            element['tienda'] = venta.tienda
            element['precio'] = venta.precio
            return {'mensaje': 'Venta actualizada'}
    return {'mensaje': 'Venta no encontrada'}

@app.delete('/ventas/{id}', tags=['Ventas'])
def delete_venta(id: int):
    for venta in ventas:
        if venta['id'] == id:
            ventas.remove(venta)
            return {'mensaje': 'Venta eliminada'}
    return {'mensaje': 'Venta no encontrada'}










