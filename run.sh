# Now that we have set up both the backend and frontend, 
# you can start the application by following these steps:
# First, start the backend server:

cd /Users/zeyichen/Documents/研二spring/user_interface/arxiv_recommender/backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload


# In a new terminal, start the frontend development server:

cd /Users/zeyichen/Documents/研二spring/user_interface/arxiv_recommender/frontend
npm install
npm start