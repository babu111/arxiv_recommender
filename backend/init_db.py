from app.database import engine, SessionLocal
from app.models import Base, User, Paper, UserPreference
from app.routers.auth import get_password_hash
from datetime import datetime
import random
import os

# Delete existing database file if it exists
if os.path.exists("arxiv_recommender.db"):
    os.remove("arxiv_recommender.db")
    print("Deleted existing database")

# Create database tables
Base.metadata.create_all(bind=engine)
print("Created tables")

# Create sample data
db = SessionLocal()

# Create sample users
users = [
    {"email": "user1@example.com", "password": "password1"},
    {"email": "user2@example.com", "password": "password2"},
    {"email": "user3@example.com", "password": "password3"},
    {"email": "dev@example.com", "password": "devpass"}
]

for user_data in users:
    hashed_password = get_password_hash(user_data["password"])
    user = User(email=user_data["email"], hashed_password=hashed_password)
    db.add(user)
print("Added users")

# Create sample papers
sample_papers = [
]

for paper_data in sample_papers:
    paper = Paper(**paper_data)
    db.add(paper)
print("Added papers")

# Commit to save the users and papers
db.commit()

# Refresh the session to get the IDs
db.close()
db = SessionLocal()

# Get users and papers
users = db.query(User).all()
papers = db.query(Paper).all()

# Create user preferences (ratings)
for user in users:
    for paper in papers:
        # Not all users rate all papers (random)
        if random.random() > 0.3:  # 70% chance of rating
            rating = random.randint(1, 5)
            pref = UserPreference(
                user_id=user.id,
                paper_id=paper.id,
                rating=rating,
                timestamp=datetime.now()
            )
            db.add(pref)
print("Added user preferences")

# Commit all changes
db.commit()
db.close()

print("Database initialization complete with sample data!") 