# arXiv Paper Recommender - Streamlit Frontend

This is a Streamlit-based frontend for the arXiv Paper Recommender system.

## Setup Instructions

1. **Create a Python virtual environment:**
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment:**
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

## Features

- View recommended arXiv papers
- Rate papers to improve future recommendations
- Fetch daily papers from arXiv

## Usage

- Make sure the backend API server is running on `http://localhost:8000` before starting the Streamlit frontend
- The app currently uses a mock authentication token for development purposes
- When you're ready to implement proper authentication, modify the headers in `app.py`

## Requirements

- Python 3.8+
- Streamlit 1.30.0+
- Requests 2.31.0+
- Pandas 2.1.3+ 