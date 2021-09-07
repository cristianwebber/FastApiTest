from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status
from ..hashing import Hash

def get_all(db: Session):
    rows = db.query(models.Backlog).all()
    return rows

def get(id: int, db: Session):
    row = db.query(models.Backlog).filter(models.Backlog.id == id).first()
    if not row:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Backlog with the id {id} not found.",
        )
    return row

def create(request: schemas.Backlog, db: Session):
    row = models.Backlog(
        title=request.title,
        description=request.description,
        status=request.status,
        start_date=request.start_date,
        end_date=request.end_date)
    
    db.add(row)
    db.commit()
    db.refresh(row)
    return row

def destroy(id: int, db: Session):
    row = db.query(models.Backlog).filter(models.Backlog.id == id)

    if not row.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Backlog with id {id} not found."
        )

    row.delete(synchronize_session=False)
    db.commit()
    return "done"


def update(id: int, request: schemas.Backlog, db: Session):
    row = db.query(models.Backlog).filter(models.Backlog.id == id)

    if not row.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Backlog with id {id} not found."
        )

    row.update(request)
    db.commit()
    return "updated"


