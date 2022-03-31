from typing import List
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from ..db import get_db
from .crud import JobCRUD
from .schemas import Job, NewJob


router = APIRouter()


@router.get("/get_all")
async def get_all(
    request: Request,
    db: Session = Depends(get_db)):
    all_jobs = await JobCRUD.get_all(db)
    return all_jobs


@router.post("/create_job")
async def create_job(
    user_id: int,
    content: NewJob,
    request: Request, 
    db: Session = Depends(get_db)):
    job = await JobCRUD.create(db, user_id, content)
    return job


@router.get("/get_by_id")
async def get_by_id(
    id: int, 
    request: Request, 
    db: Session = Depends(get_db)
    ):
    job = await JobCRUD.get_by_id(db, id)
    return job


@router.put("/update_job")
async def update_job(
    id: int,
    user_id: int,
    content: NewJob,
    request: Request, 
    db: Session = Depends(get_db)
    ):
    job = await JobCRUD.update(db, id, user_id, content)
    return job


@router.delete("/delete")
async def delete_job(
    id: str, 
    request: Request, db: 
    Session = Depends(get_db)
    ):
    deleted_job = await JobCRUD.delete(db, id)
    return deleted_job