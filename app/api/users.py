from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserRead
from app.core.rfm import r_score, f_score, m_score, segment as rfm_segment

router = APIRouter()

@router.post("", response_model=UserRead, status_code=201)
def create(payload: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.external_id == payload.external_id).first():
        raise HTTPException(409, "external_id exists")
    u = User(**payload.model_dump())
    u.r_score = r_score(u.recency_days)
    u.f_score = f_score(u.frequency)
    u.m_score = m_score(u.monetary)
    u.rfm_segment = rfm_segment(u.r_score, u.f_score, u.m_score)
    db.add(u)
    db.commit()
    db.refresh(u)
    return u

@router.get("", response_model=List[UserRead])
def list_users(limit: int = 500, db: Session = Depends(get_db)):
    return db.query(User).limit(limit).all()
