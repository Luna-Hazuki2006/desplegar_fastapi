from typing import Union, List
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status
from datetime import datetime

app = FastAPI()

class Estudiante(BaseModel): 
    cedula : str
    nombres : str
    apellidos : str
    nacimiento : datetime

estudiantes : List[Estudiante] = []

@app.get('/estudiantes')
async def leer_raiz(): 
    return estudiantes

@app.get('/estudiante/{cedula}')
async def buscar(cedula : str): 
    for esto in estudiantes: 
        if esto.cedula == cedula: 
            return esto
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail="No se pudo encontrar un estudiante con tal cédula"
    )

@app.post('/estudiante')
async def crear(estudiante : Estudiante): 
    for esto in estudiantes: 
        if esto.cedula == estudiante.cedula: 
            return HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="No se puede crear un estudiante con una cédula repetida"
            )
    estudiantes.append(estudiante)
    return estudiante
        
@app.put('/estudiante/{cedula}')
async def actualizar(cedula : str, estudiante : Estudiante): 
    if cedula != estudiante.cedula: 
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="La cédula de los parámetros no puede ser diferente a la cédula del estudiante"
        )
    for i in range(len(estudiantes)): 
        if estudiantes[i].cedula == estudiante.cedula: 
            estudiantes[i] = estudiante
            return estudiantes[i]
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail="No se pudo encontrar un estudiante con tal cédula"
    )

@app.delete('/estudiante/{cedula}')
async def eliminar(cedula : str): 
    for i in range(len(estudiantes)): 
        if estudiantes[i].cedula == cedula: 
            estudiante = estudiantes[i]
            estudiantes.remove(estudiante)
            return estudiante
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail="No se pudo encontrar un estudiante con tal cédula"
    )
