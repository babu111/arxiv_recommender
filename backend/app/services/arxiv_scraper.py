import arxiv
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from ..models import Paper
from typing import List

class ArxivScraper:
    def __init__(self):
        self.client = arxiv.Client()
        
    def search_papers(self, query: str = "cat:cs.LG", max_results: int = 100) -> List[arxiv.Result]:
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending
        )
        return list(self.client.results(search))
    
    def save_papers(self, db: Session, papers: List[arxiv.Result]):
        for paper in papers:
            # Check if paper already exists
            existing_paper = db.query(Paper).filter(Paper.arxiv_id == paper.entry_id).first()
            if not existing_paper:
                new_paper = Paper(
                    arxiv_id=paper.entry_id,
                    title=paper.title,
                    authors=", ".join(author.name for author in paper.authors),
                    abstract=paper.summary,
                    categories=", ".join(paper.categories),
                    published_date=paper.published,
                    pdf_url=paper.pdf_url
                )
                db.add(new_paper)
        
        db.commit()
    
    def fetch_daily_papers(self, db: Session):
        """Fetch papers from the last 24 hours"""
        papers = self.search_papers()
        self.save_papers(db, papers)
        return papers 