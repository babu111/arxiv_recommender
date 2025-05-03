import sys
import os
import pytest
from fastapi.testclient import TestClient

# Ensure the app module can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))
from backend.app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to arXiv Paper Recommender API"} 
    
    
    
# TO run the test, run
# pytest tests/test_main.py