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
    
    def get_content_based_recommendations(self, db: Session, user_id: int, n_recommendations: int = 10) -> List[Dict]:
        """Fallback content-based recommendations when collaborative filtering fails"""
        # Get user's rated papers
        user_preferences = db.query(UserPreference).filter(UserPreference.user_id == user_id).all()
        
        if not user_preferences:
            # If no ratings, return recent papers
            papers = db.query(Paper).order_by(Paper.published_date.desc()).limit(n_recommendations).all()
            return [
                {
                    'paper': paper,
                    'predicted_rating': 3.0  # Default neutral rating
                }
                for paper in papers
            ]
        
        # Get papers the user has already rated
        rated_paper_ids = {pref.paper_id for pref in user_preferences}
        
        # Get average rating for this user
        avg_rating = sum(pref.rating for pref in user_preferences) / len(user_preferences)
        
        # Get ALL unrated papers (not just 50)
        unrated_papers = db.query(Paper).filter(~Paper.id.in_(rated_paper_ids)).all()
        
        # Simple content-based: prefer papers from categories the user liked
        liked_categories = set()
        for pref in user_preferences:
            if pref.rating >= 4:  # Consider 4+ as "liked"
                paper = db.query(Paper).filter(Paper.id == pref.paper_id).first()
                if paper:
                    categories = paper.categories.split(', ')
                    liked_categories.update(categories)
        
        recommendations = []
        for paper in unrated_papers:
            predicted_rating = avg_rating  # Start with user's average
            
            # Boost rating if paper has liked categories
            if liked_categories:
                paper_categories = set(paper.categories.split(', '))
                common_categories = liked_categories.intersection(paper_categories)
                if common_categories:
                    predicted_rating += 0.5 * len(common_categories)
            
            # Cap the rating at 5.0
            predicted_rating = min(predicted_rating, 5.0)
            
            recommendations.append({
                'paper': paper,
                'predicted_rating': predicted_rating
            })
        
        # Sort by predicted rating and return top N from ALL papers
        recommendations.sort(key=lambda x: x['predicted_rating'], reverse=True)
        return recommendations[:n_recommendations]
    
    def get_recommendations(self, db: Session, user_id: int, n_recommendations: int = 10) -> List[Dict]:
        """Get paper recommendations for a user"""
        # Get user's rated papers first
        user_preferences = db.query(UserPreference).filter(UserPreference.user_id == user_id).all()
        rated_paper_ids = {pref.paper_id for pref in user_preferences}
        
        # Get ALL papers in the database
        all_papers = db.query(Paper).all()
        unrated_papers = [paper for paper in all_papers if paper.id not in rated_paper_ids]
        
        if not unrated_papers:
            return []  # User has rated all papers
        
        recommendations = []
        
        # Try collaborative filtering first
        if self.user_paper_matrix is None:
            self.build_user_paper_matrix(db)
            
        if self.paper_similarity is None:
            self.compute_paper_similarity()
            
        # Check if we have enough data for collaborative filtering
        if (self.user_paper_matrix is not None and 
            self.paper_similarity is not None and 
            user_id in self.user_paper_matrix.index and
            len(user_preferences) > 0):
            
            # Get user's ratings from the matrix
            user_ratings = self.user_paper_matrix.loc[user_id]
            rated_papers_in_matrix = user_ratings[user_ratings > 0].index
            
            # Calculate predictions for ALL unrated papers
            collaborative_predictions = {}
            
            for paper in unrated_papers:
                paper_id = paper.id
                
                # Check if this paper exists in the similarity matrix
                if paper_id in self.user_paper_matrix.columns:
                    try:
                        paper_idx = self.user_paper_matrix.columns.get_loc(paper_id)
                        similar_papers = self.paper_similarity[paper_idx]
                        
                        # Weight the ratings by paper similarity
                        weighted_ratings = []
                        similarities = []
                        for rated_paper in rated_papers_in_matrix:
                            rated_idx = self.user_paper_matrix.columns.get_loc(rated_paper)
                            similarity = similar_papers[rated_idx]
                            rating = user_ratings[rated_paper]
                            weighted_ratings.append(similarity * rating)
                            similarities.append(similarity)
                            
                        if weighted_ratings and sum(similarities) > 0:
                            pred_rating = sum(weighted_ratings) / sum(similarities)
                            collaborative_predictions[paper_id] = pred_rating
                    except (KeyError, IndexError):
                        continue
            
            # For papers with collaborative predictions, use them
            for paper in unrated_papers:
                if paper.id in collaborative_predictions:
                    recommendations.append({
                        'paper': paper,
                        'predicted_rating': collaborative_predictions[paper.id]
                    })
                else:
                    # For papers not in the matrix (newly fetched), use content-based approach
                    if user_preferences:
                        avg_rating = sum(pref.rating for pref in user_preferences) / len(user_preferences)
                        
                        # Get liked categories
                        liked_categories = set()
                        for pref in user_preferences:
                            if pref.rating >= 4:
                                rated_paper = db.query(Paper).filter(Paper.id == pref.paper_id).first()
                                if rated_paper:
                                    categories = rated_paper.categories.split(', ')
                                    liked_categories.update(categories)
                        
                        predicted_rating = avg_rating
                        
                        # Boost rating if paper has liked categories
                        if liked_categories:
                            paper_categories = set(paper.categories.split(', '))
                            common_categories = liked_categories.intersection(paper_categories)
                            if common_categories:
                                predicted_rating += 0.5 * len(common_categories)
                        
                        predicted_rating = min(predicted_rating, 5.0)
                        
                        recommendations.append({
                            'paper': paper,
                            'predicted_rating': predicted_rating
                        })
                    else:
                        recommendations.append({
                            'paper': paper,
                            'predicted_rating': 3.0
                        })
        
        else:
            # Fallback to content-based for all papers
            return self.get_content_based_recommendations(db, user_id, n_recommendations)
        
        # Sort ALL recommendations by predicted rating and return top N
        recommendations.sort(key=lambda x: x['predicted_rating'], reverse=True)
        return recommendations[:n_recommendations] 