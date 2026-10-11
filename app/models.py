from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    external_id = Column(String, unique=True, index=True)
    recency_days = Column(Integer, default=0)
    frequency = Column(Integer, default=0)
    monetary = Column(Float, default=0.0)
    tenure_days = Column(Integer, default=0)
    r_score = Column(Integer, default=0)
    f_score = Column(Integer, default=0)
    m_score = Column(Integer, default=0)
    rfm_segment = Column(String, index=True)
    kmeans_cluster = Column(Integer, index=True)
    abc_class = Column(String, index=True)
    created_at = Column(DateTime, server_default=func.now())
