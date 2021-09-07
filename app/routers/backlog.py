from typing import List
from fastapi import APIRouter
from .. import database, schemas, models, oauth2
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from ..repository import backlog

router = APIRouter(prefix="/backlog", tags=["Backlog"])

get_db = database.get_db

@router.get("/", response_model=List[schemas.Backlog])
def get_all(
    db: Session = Depends(get_db)):
    return backlog.get_all(db)


@router.get("/{id}", status_code=200, response_model=schemas.Backlog)
def get(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user)
):
    return backlog.get(id, db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(
    request: schemas.Backlog, 
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user)
):
    return backlog.create(request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return backlog.destroy(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(
    id: int,
    request: schemas.Backlog,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return backlog.update(id, request, db)




