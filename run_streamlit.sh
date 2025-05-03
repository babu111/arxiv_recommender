#!/bin/bash

cd /Users/zeyichen/Documents/研二spring/user_interface/arxiv_recommender
# Navigate to backend
cd backend

# Activate virtual environment
source venv/bin/activate || { echo "Failed to activate backend virtual environment"; exit 1; }

# Initialize the database
echo "Initializing database with sample data..."
python init_db.py || { echo "Failed to initialize database"; exit 1; }

# Start the backend server in the background
echo "Starting FastAPI backend server..."
uvicorn app.main:app --reload &
BACKEND_PID=$!



# in a new terminal, start the Streamlit frontend

# Start the Streamlit frontend
echo "Starting Streamlit frontend..."
cd /Users/zeyichen/Documents/研二spring/user_interface/arxiv_recommender
cd frontend_streamlit


# Check if virtual environment exists, if not, create it
if [ ! -d "venv" ]; then
    echo "Creating Streamlit virtual environment..."
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

# Run Streamlit app
streamlit run app.py

# When Streamlit is closed, also stop the backend
echo "Shutting down backend server (PID: $BACKEND_PID)..."
kill $BACKEND_PID 