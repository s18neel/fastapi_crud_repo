from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import BookSchema, Request, Response, RequestBook

import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
async def create_book_service(request: RequestBook, db: Session = Depends(get_db)):
    crud.create_book(db, book=request.parameter)
    return Response(status="Ok", code="200", message="Book created successfully", result=None).dict(exclude_none=True)

@router.get("/")
async def get_books(skip: int = 0, limit:int = 0, db: Session = Depends(get_db)):
    _books = crud.get_book(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_books)

@router.patch("/update")
async def update_books(request:RequestBook, db: Session = Depends(get_db)):
    _books = crud.update_book(db, book_id=request.parameter.id, title= request.parameter.title, description=request.parameter.description) #type:ignore
    return Response(status="Ok", code="200", message="Success update data", result=_books)

@router.delete('/delete')
async def delete_books(request:RequestBook, db: Session = Depends(get_db)):
    crud.remove_book(db, book_id=request.parameter.id)  #type:ignore
    return Response(status="Ok", code="200", message="Book Deleted Successfully").dict(exclude_none=True)  #type:ignore