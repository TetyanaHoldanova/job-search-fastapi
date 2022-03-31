from typing import List
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from ..db import get_db
from .crud import UserCRUD
from .schemas import User, NewUser


router = APIRouter()


@router.get("/get_all")
async def get_all(
    request: Request,
    db: Session = Depends(get_db)):
    all_users = await UserCRUD.get_all(db)
    return all_users


@router.post("/create_user")
async def create_user(
    content: NewUser,
    request: Request, 
    db: Session = Depends(get_db)):
    user = await UserCRUD.create(db, content)
    return user


@router.get("/get_by_id")
async def get_by_id(
    id: int, 
    request: Request, 
    db: Session = Depends(get_db)
    ):
    user = await UserCRUD.get_by_id(db, id)
    return user


@router.get("/get_by_email")
async def get_by_email(
    email: str, 
    request: Request, 
    db: Session = Depends(get_db)
    ):
    user = await UserCRUD.get_by_email(db, email)
    return user


@router.put("/update_user")
async def update_user(
    id: int,
    content: NewUser,
    request: Request, 
    db: Session = Depends(get_db)):
    user = await UserCRUD.update(db, id, content)
    return user