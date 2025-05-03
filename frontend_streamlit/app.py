import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# Configure API
API_URL = "http://localhost:8000"
MOCK_TOKEN = "mock_development_token"
HEADERS = {
    "Authorization": f"Bearer {MOCK_TOKEN}",
    "Content-Type": "application/json"
}

# Page configuration
st.set_page_config(
    page_title="arXiv Paper Recommender",
    page_icon="📚",
    layout="wide"
)

# Title
st.title("arXiv Paper Recommender")

# Sidebar
st.sidebar.header("Actions")
if st.sidebar.button("Fetch Daily Papers"):
    try:
        response = requests.post(f"{API_URL}/api/papers/fetch-daily", headers=HEADERS)
        if response.status_code == 200:
            st.sidebar.success("Successfully fetched daily papers!")
        else:
            st.sidebar.error(f"Failed to fetch papers: {response.text}")
    except Exception as e:
        st.sidebar.error(f"Error: {str(e)}")

# Main content area
def get_recommendations():
    try:
        # Using a fixed user ID since we're bypassing authentication
        user_id = 1
        response = requests.get(f"{API_URL}/api/papers/recommendations/{user_id}", headers=HEADERS)
        
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to fetch recommendations: {response.text}")
            return []
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return []

def rate_paper(paper_id, rating):
    try:
        user_id = 1  # Fixed user ID for development
        response = requests.post(
            f"{API_URL}/api/papers/{paper_id}/rate",
            json={"user_id": user_id, "rating": rating},
            headers=HEADERS
        )
        
        if response.status_code == 200:
            st.success("Paper rated successfully!")
            # Refresh the page to show updated recommendations
            st.experimental_rerun()
        else:
            st.error(f"Failed to rate paper: {response.text}")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Get recommendations
recommendations = get_recommendations()

if not recommendations:
    st.info("No recommendations available. Try fetching daily papers from the sidebar!")
else:
    st.subheader(f"Showing {len(recommendations)} recommended papers")
    
    # Display each paper as a card
    for recommendation in recommendations:
        paper = recommendation['paper']
        predicted_rating = recommendation['predicted_rating']
        
        with st.expander(f"{paper['title']} - Predicted Rating: {predicted_rating:.1f}/5"):
            st.markdown(f"**Authors:** {paper['authors']}")
            st.markdown(f"**Categories:** {paper['categories']}")
            st.markdown(f"**Abstract:**")
            st.markdown(paper['abstract'])
            
            col1, col2 = st.columns([1, 3])
            with col1:
                st.link_button("View PDF", paper['pdf_url'], use_container_width=True)
            
            with col2:
                # Rating widget
                st.write("Rate this paper:")
                user_rating = st.slider(
                    "Your rating",
                    min_value=1,
                    max_value=5,
                    value=int(predicted_rating) if predicted_rating else 3,
                    key=f"rating_{paper['id']}"
                )
                
                if st.button("Submit Rating", key=f"submit_{paper['id']}"):
                    rate_paper(paper['id'], user_rating)

# Footer
st.markdown("---")
st.markdown("© 2023 arXiv Paper Recommender") 