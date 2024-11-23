from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI()

class Curso(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    nivel: str
    duration: int

curso_db = []

@app.get("/cursos/", response_model=List[Curso])
def getCursos():
    return curso_db

@app.post("/cursos/", response_model=Curso)
def addCurso(curso: Curso):
    curso.id = str(uuid.uuid4())
    curso_db.append(curso)
    return curso

@app.get("/cursos/{curso_id}", response_model=Curso)
def getCurso(curso_id: str):
    curso = next((curso for curso in curso_db if curso.id == curso_id), None) # con next tomamos la primera coincidencia
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso not found")
    return curso

@app.put("/cursos/{id}", response_model=Curso)
def updateCurso(id: str, item: Curso):
    curso = next((curso for curso in curso_db if curso.id == id), None) 
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso not found")
    
    item.id = curso.id
    index = curso_db.index(curso) # buscamos el indice del curso
    curso_db[index] = item
    return item

@app.delete("/cursos/{id}", response_model=Curso)
def deleteCurso(id: str):
    curso = next((curso for curso in curso_db if curso.id == id), None)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso not found")
    curso_db.remove(curso)
    return curso

# uvicorn main:app --reload
# render 
# render deploy fastapi app
# pip install re...txt


