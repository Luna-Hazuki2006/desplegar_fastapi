from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def leer_raiz(): 
    return {'mensaje': 'Hola desde Koyeb :3'}