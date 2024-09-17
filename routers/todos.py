from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
import schemas
import crud
from database import SessionLocal

router = APIRouter(
    prefix="/todos"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.ToDoRequest, db: Session = Depends(get_db)):
    todo = crud.create_todo(db, todo)
    return todo

@router.get("", response_model=List[schemas.ToDoResponse])
def get_todos(completed: bool = None, db: Session = Depends(get_db)):
    todos = crud.read_todos(db, completed)
    return todos

@router.get("/{id}")
def get_todo_by_id(id: int, db: Session = Depends(get_db)):
    todo = crud.read_todo(db, id)
    if todo is None:
        raise HTTPException(status_code=404, detail="to do not found")
    return todo

@router.put("/{id}")
def update_todo(id: int, todo: schemas.ToDoRequest, db: Session = Depends(get_db)):
    todo = crud.update_todo(db, id, todo)
    if todo is None:
        raise HTTPException(status_code=404, detail="to do not found")
    return todo

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_todo(id: int, db: Session = Depends(get_db)):
    res = crud.delete_todo(db, id)
    if res is None:
        raise HTTPException(status_code=404, detail="to do not found")

##Summary:

#Router Setup: Organizes all the "to-do" routes under /todos.
#Database Session: A helper function manages database connections.
#CRUD Operations: Routes handle creating, reading, updating, and deleting "to-do" items.
#POST /todos: Create a new to-do.
#GET /todos: Get all to-dos, optionally filtering by completion status.
#GET /todos/{id}: Get a specific to-do by ID.
#PUT /todos/{id}: Update a specific to-do by ID.
#DELETE /todos/{id}: Delete a specific to-do by ID.
#Error Handling: If an item is not found (like when trying to update or delete), it raises a 404 HTTP error.
#This setup makes it easy to manage "to-do" items in a structured and RESTful way using FastAPI.##