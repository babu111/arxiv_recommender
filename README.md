# arXiv Paper Recommender

A web application that recommends arXiv papers based on your interests and reading history. The application scrapes daily papers from arXiv and uses a collaborative filtering algorithm to provide personalized recommendations.

## Features

- Daily arXiv paper scraping (focusing on machine learning papers)
- User authentication
- Personalized paper recommendations
- Paper rating system
- Reading history tracking
- Modern and responsive UI

## Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- scikit-learn
- arXiv API

### Frontend
- React
- TypeScript
- Material-UI
- Axios

## Setup

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the backend server:
```bash
uvicorn app.main:app --reload
```

The backend server will start at http://localhost:8000

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The frontend application will start at http://localhost:3000

## Usage

1. Register a new account or log in with existing credentials
2. Browse through recommended papers on the home page
3. Rate papers to improve recommendations
4. Click "Fetch Daily Papers" to get the latest papers from arXiv
5. View paper PDFs by clicking the "View PDF" button

## API Documentation

Once the backend server is running, you can access the API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Contributing

Feel free to submit issues and enhancement requests!
