from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Paper

# Connect to the database
engine = create_engine("sqlite:///arxiv_recommender.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

# Query the papers table
papers = db.query(Paper).all()

# Print the papers
for paper in papers:
    print(f"Title: {paper.title}, Authors: {paper.authors}, Published Date: {paper.published_date}")

# Close the session
db.close()