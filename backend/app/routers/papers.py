from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import Paper, UserPreference
from ..services.arxiv_scraper import ArxivScraper
from ..services.recommender import PaperRecommender
from datetime import datetime

router = APIRouter()
scraper = ArxivScraper()
recommender = PaperRecommender()

@router.get("/papers/", response_model=List[dict])
async def get_papers(db: Session = Depends(get_db)):
    papers = db.query(Paper).all()
    return [
        {
            "id": paper.id,
            "arxiv_id": paper.arxiv_id,
            "title": paper.title,
            "authors": paper.authors,
            "abstract": paper.abstract,
            "categories": paper.categories,
            "published_date": paper.published_date,
            "pdf_url": paper.pdf_url
        }
        for paper in papers
    ]

@router.get("/papers/recommendations/{user_id}")
async def get_recommendations(user_id: int, db: Session = Depends(get_db)):
    recommendations = recommender.get_recommendations(db, user_id)
    return recommendations

@router.post("/papers/fetch-daily")
async def fetch_daily_papers(db: Session = Depends(get_db)):
    papers = scraper.fetch_daily_papers(db)
    return {"message": f"Fetched {len(papers)} new papers"}

@router.post("/papers/{paper_id}/rate")
async def rate_paper(
    paper_id: int,
    user_id: int,
    rating: float,
    db: Session = Depends(get_db)
):
    if rating < 1 or rating > 5:
        raise HTTPException(status_code=400, detail="Rating must be between 1 and 5")
        
    paper = db.query(Paper).filter(Paper.id == paper_id).first()
    if not paper:
        raise HTTPException(status_code=404, detail="Paper not found")
        
    # Update or create user preference
    preference = db.query(UserPreference).filter(
        UserPreference.user_id == user_id,
        UserPreference.paper_id == paper_id
    ).first()
    
    if preference:
        preference.rating = rating
        preference.timestamp = datetime.utcnow()
    else:
        preference = UserPreference(
            user_id=user_id,
            paper_id=paper_id,
            rating=rating,
            timestamp=datetime.utcnow()
        )
        db.add(preference)
        
    db.commit()
    return {"message": "Rating saved successfully"} 