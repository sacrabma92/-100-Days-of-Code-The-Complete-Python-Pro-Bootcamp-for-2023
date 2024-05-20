
from fastapi import FastAPI

#Crear una instancia de FastAPI
app = FastAPI()
app.title = 'Aplicacion de Ventas'
app.version = '0.0.1'

# Crear punto de entreda
@app.get("/", tags=['Inicio'])  #Cavmio de etiqueta en Documentacion
def mensaje():
    return "Bienvenido, a FastAPI"