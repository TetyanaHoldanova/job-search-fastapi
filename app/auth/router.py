from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..db import get_db
from .schemas import Token, Login
from ..users.crud import UserCRUD
from ..security import verify_password, create_access_token


router = APIRouter()


@router.post("/login", response_model=Token)
async def login(
    login: Login,
    db: Session = Depends(get_db)
    ):
    user = await UserCRUD.get_by_email(db, login.email)
    if user is None or not verify_password(login.password, user.hashed_password): 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    return Token(
        access_token=create_access_token({"sub: user.email"}),
        token_type="Bearer"
    )
