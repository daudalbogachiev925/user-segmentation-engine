from typing import Optional, List
from pydantic import BaseModel

class UserBase(BaseModel):
    external_id: str
    recency_days: int
    frequency: int
    monetary: float
    tenure_days: int = 0

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int
    r_score: Optional[int]
    f_score: Optional[int]
    m_score: Optional[int]
    rfm_segment: Optional[str]
    kmeans_cluster: Optional[int]
    abc_class: Optional[str]

    class Config:
        from_attributes = True

class SegmentSummary(BaseModel):
    segment: str
    count: int
    avg_monetary: float
    total_monetary: float
