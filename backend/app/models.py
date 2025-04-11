from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    preferences = relationship("UserPreference", back_populates="user")
    reading_history = relationship("ReadingHistory", back_populates="user")

class Paper(Base):
    __tablename__ = "papers"

    id = Column(Integer, primary_key=True, index=True)
    arxiv_id = Column(String, unique=True, index=True)
    title = Column(String)
    authors = Column(String)
    abstract = Column(String)
    categories = Column(String)
    published_date = Column(DateTime)
    pdf_url = Column(String)
    
    preferences = relationship("UserPreference", back_populates="paper")
    reading_history = relationship("ReadingHistory", back_populates="paper")

class UserPreference(Base):
    __tablename__ = "user_preferences"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    paper_id = Column(Integer, ForeignKey("papers.id"))
    rating = Column(Float)  # User's rating for the paper (1-5)
    timestamp = Column(DateTime)
    
    user = relationship("User", back_populates="preferences")
    paper = relationship("Paper", back_populates="preferences")

class ReadingHistory(Base):
    __tablename__ = "reading_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    paper_id = Column(Integer, ForeignKey("papers.id"))
    read_date = Column(DateTime)
    
    user = relationship("User", back_populates="reading_history")
    paper = relationship("Paper", back_populates="reading_history") 