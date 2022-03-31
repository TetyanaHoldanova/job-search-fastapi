from dataclasses import dataclass
from sqlalchemy.orm import Session
from typing import List, Optional
import datetime

from . import models, schemas
from ..security import hash_password


@dataclass
class UserCRUD:
    async def get_all(db: Session) -> List[dict]:
        rows = db.query(models.Users).all()
        return [row.__dict__ for row in rows]


    async def create(db: Session, u: schemas.NewUser) -> models.Users:
        user = models.Users(
            id = None,
            name=u.name,
            email=u.email,
            hashed_password=hash_password(u.password),
            is_company=u.is_company,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )
        db.add(user)
        db.commit()
        db.refresh(user)

        return user.__dict__

    
    async def get_by_id(db: Session, id: int) -> Optional[schemas.User]:
        row = db.query(models.Users).filter_by(id=id).first()
        return row.__dict__

    
    async def get_by_email(db: Session, email: str) -> schemas.User:
        row = db.query(models.Users).filter_by(email=email).first()
        return row.__dict__


    async def update(db: Session, id: int, u: schemas.NewUser) -> schemas.User:
         user = models.Users(
            id=id,
            name=u.name,
            email=u.email,
            hashed_password=hash_password(u.password2),
            is_company=u.is_company,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
         )
         row = db.query(models.Users).filter_by(id=id).first()
         row.name = user.name
         row.email = user.email
         row.hashed_password = user.hashed_password
         row.updated_at = user.updated_at

         db.add(row)
         db.commit()
         db.refresh(row)

         return user.__dict__

 