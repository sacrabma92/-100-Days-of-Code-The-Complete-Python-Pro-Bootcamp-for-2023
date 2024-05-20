from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Body

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
def agregar_venta(
    id: int = Body(),
    nombre: str = Body(),
    fecha: str = Body(),
    tienda: str = Body(),
    precio: float = Body(),
):
  ventas.append({'id': id, 'nombre': nombre, 'fecha': fecha, 'tienda': tienda, 'precio': precio})
  return {'mensaje': 'Venta agregada correctamente'}
    
@app.put('/ventas/{id}', tags=['Ventas'])
def actualizar_venta(
    id: int, 
    nombre: str = Body(), 
    fecha: str = Body(), 
    tienda: str = Body(), 
    precio: float = Body()
    ):
    for element in ventas:
        if element['id'] == id:
            element['nombre'] = nombre
            element['fecha'] = fecha
            element['tienda'] = tienda
            element['precio'] = precio
            return {'mensaje': 'Venta actualizada'}
    return {'mensaje': 'Venta no encontrada'}

@app.delete('/ventas/{id}', tags=['Ventas'])
def delete_venta(id: int):
    for venta in ventas:
        if venta['id'] == id:
            ventas.remove(venta)
            return {'mensaje': 'Venta eliminada'}
    return {'mensaje': 'Venta no encontrada'}










