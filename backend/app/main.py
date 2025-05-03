from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import uvicorn
from .database import engine
from .models import Base  # Import Base from models instead
from .routers import papers, auth

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="arXiv Paper Recommender")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["authentication"])
app.include_router(papers.router, prefix="/api", tags=["papers"])

@app.get("/")
async def root():
    return {"message": "Welcome to arXiv Paper Recommender API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 