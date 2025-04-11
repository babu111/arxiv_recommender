import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sqlalchemy.orm import Session
from ..models import Paper, UserPreference, User
from typing import List, Dict
import pandas as pd

class PaperRecommender:
    def __init__(self):
        self.user_paper_matrix = None
        self.paper_similarity = None
        
    def build_user_paper_matrix(self, db: Session):
        """Build user-paper rating matrix"""
        preferences = db.query(UserPreference).all()
        
        # Create DataFrame
        data = []
        for pref in preferences:
            data.append({
                'user_id': pref.user_id,
                'paper_id': pref.paper_id,
                'rating': pref.rating
            })
        
        if not data:
            return None
            
        df = pd.DataFrame(data)
        self.user_paper_matrix = df.pivot(
            index='user_id',
            columns='paper_id',
            values='rating'
        ).fillna(0)
        
        return self.user_paper_matrix
    
    def compute_paper_similarity(self):
        """Compute similarity between papers based on user ratings"""
        if self.user_paper_matrix is None:
            return None
            
        # Transpose matrix to get paper-user matrix
        paper_user_matrix = self.user_paper_matrix.T
        
        # Compute cosine similarity between papers
        self.paper_similarity = cosine_similarity(paper_user_matrix)
        
        return self.paper_similarity
    
    def get_recommendations(self, db: Session, user_id: int, n_recommendations: int = 10) -> List[Dict]:
        """Get paper recommendations for a user"""
        if self.user_paper_matrix is None:
            self.build_user_paper_matrix(db)
            
        if self.paper_similarity is None:
            self.compute_paper_similarity()
            
        if self.user_paper_matrix is None or self.paper_similarity is None:
            return []
            
        # Get user's rated papers
        user_ratings = self.user_paper_matrix.loc[user_id]
        rated_papers = user_ratings[user_ratings > 0].index
        
        # Get unrated papers
        unrated_papers = user_ratings[user_ratings == 0].index
        
        if len(unrated_papers) == 0:
            return []
            
        # Calculate predicted ratings for unrated papers
        predictions = []
        for paper_id in unrated_papers:
            paper_idx = self.user_paper_matrix.columns.get_loc(paper_id)
            similar_papers = self.paper_similarity[paper_idx]
            
            # Weight the ratings by paper similarity
            weighted_ratings = []
            for rated_paper in rated_papers:
                rated_idx = self.user_paper_matrix.columns.get_loc(rated_paper)
                similarity = similar_papers[rated_idx]
                rating = user_ratings[rated_paper]
                weighted_ratings.append(similarity * rating)
                
            if weighted_ratings:
                pred_rating = sum(weighted_ratings) / sum(similar_papers)
                predictions.append((paper_id, pred_rating))
        
        # Sort by predicted rating and get top N
        predictions.sort(key=lambda x: x[1], reverse=True)
        top_papers = predictions[:n_recommendations]
        
        # Get paper details
        recommendations = []
        for paper_id, pred_rating in top_papers:
            paper = db.query(Paper).filter(Paper.id == paper_id).first()
            if paper:
                recommendations.append({
                    'paper': paper,
                    'predicted_rating': pred_rating
                })
                
        return recommendations 