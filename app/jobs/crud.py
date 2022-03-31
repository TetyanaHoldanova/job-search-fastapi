from dataclasses import dataclass
from typing import List, Optional
from dataclasses import dataclass
from sqlalchemy.orm import Session
import datetime

from . import models, schemas


@dataclass
class JobCRUD:
    async def get_all(db:Session):
        rows = db.query(models.Jobs).all()
        return [row.__dict__ for row in rows]


    async def create(db: Session, user_id: int, j: schemas.NewJob) -> schemas.Job:
        job = models.Jobs(
            id=0,
            user_id=user_id,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
            title=j.title,
            description=j.description,
            salary_from=j.salary_from,
            salary_to=j.salary_to,
            is_active=j.is_active,
        )
        db.add(job)
        db.commit()
        db.refresh(job)

        return job.__dict__


    async def update(db: Session, id: int, user_id: int, j: schemas.NewJob) -> schemas.Job:
        job = models.Jobs(
            id=id,
            user_id=user_id,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
            title=j.title,
            description=j.description,
            salary_from=j.salary_from,
            salary_to=j.salary_to,
            is_active=j.is_active,
        )
        row = db.query(models.Jobs).filter_by(id=id).first()        
        row.title = job.title
        row.description = job.description
        row.salary_from = job.salary_from
        row.salary_to = job.salary_to
        row.updated_at = job.updated_at
        row.is_active = job.is_active

        db.add(row)
        db.commit()
        db.refresh(row)

        return job.__dict__


    async def delete(db:Session, id: int):
        job = db.query(models.Jobs).filter_by(id=id).first()

        report = job.__dict__

        db.delete(job)
        db.commit()

        return report


    async def get_by_id(db: Session, id: int) -> Optional[schemas.Job]:
        job = db.query(models.Jobs).filter_by(id=id).first()
        if job is None:
            return None
        return job.__dict__