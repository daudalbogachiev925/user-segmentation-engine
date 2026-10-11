from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from collections import defaultdict
from app.database import get_db
from app.models import User
from app.schemas import SegmentSummary
from app.core.kmeans_seg import fit_clusters
from app.core.abc import abc_classify
from app.config import settings

router = APIRouter()

@router.post("/recompute")
def recompute(db: Session = Depends(get_db)):
    users = db.query(User).all()
    if len(users) < 5:
        return {"error": "not enough users"}
    labels, _ = fit_clusters(users, settings.K_CLUSTERS)
    for u, lbl in zip(users, labels):
        u.kmeans_cluster = int(lbl)
    abc_map = abc_classify(users)
    for u in users:
        u.abc_class = abc_map.get(u.id, "C")
    db.commit()
    return {"clusters": settings.K_CLUSTERS, "users": len(users)}

@router.get("/rfm", response_model=List[SegmentSummary])
def rfm_summary(db: Session = Depends(get_db)):
    rows = db.query(User.rfm_segment,
                    func.count(User.id),
                    func.avg(User.monetary),
                    func.sum(User.monetary)) \
             .group_by(User.rfm_segment).all()
    return [SegmentSummary(segment=r[0] or "Others", count=r[1],
                            avg_monetary=float(r[2] or 0),
                            total_monetary=float(r[3] or 0))
            for r in rows]

@router.get("/abc")
def abc_summary(db: Session = Depends(get_db)):
    rows = db.query(User.abc_class, func.count(User.id),
                    func.sum(User.monetary)) \
             .group_by(User.abc_class).all()
    return [{"class": r[0] or "C", "count": r[1],
             "revenue": float(r[2] or 0)} for r in rows]

@router.get("/kmeans")
def kmeans_summary(db: Session = Depends(get_db)):
    rows = db.query(User.kmeans_cluster, func.count(User.id),
                    func.avg(User.monetary)) \
             .group_by(User.kmeans_cluster).all()
    return [{"cluster": r[0], "count": r[1], "avg_monetary": float(r[2] or 0)}
            for r in rows]
