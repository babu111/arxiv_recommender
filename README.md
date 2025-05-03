# ArXiv Paper Recommender App

## Progress 
- 5.2.2025: Able to fetch papers from arXiv api. Showing a rating bar for users to submit rating. Clicking "View PDF" takes users to arXiv paper page.
- 4.18.2025: Finished building the frontend tech stack using ReAct. The homepage is showing just fine. Plan to build the Arxiv api & recommendation system via python backend. Plan to also include a registration and login mechanism for users.

## Installation

This application is tested on macOS. No guarantee on Windows or Linux.

#### Backend Environment Setup

   ```bash
   cd /path/to/arxiv_recommender/backend
   # creating pip virtual env
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   # Create initial database
   # This will create the SQLite database when you first run the app
   uvicorn app.main:app --reload
   ```

#### Frontend Environment Setup

   ```bash
   cd /path/to/arxiv_recommender/frontend
   npm install
   ```

## Running the Application
The script to run the application is `run.sh`. Here's a breakdown of its content.
#### Start the Backend Server
```bash
cd /path/to/arxiv_recommender/backend
source venv/bin/activate
uvicorn app.main:app --reload
```

### Start the Frontend Development Server
```bash
cd /path/to/arxiv_recommender/frontend
npm start
```

## Troubleshooting

### Backend Issues
- If you encounter database issues, try deleting the existing database file and restart the server:
  ```bash
  rm backend/arxiv_recommender.db
  ```
- Ensure port 8000 is not in use by another application.

### Frontend Issues
- Check that the API URL in `frontend/src/services/api.ts` points to the correct backend URL (default: `http://localhost:8000`).
- Ensure port 3000 is not in use by another application.

## When You Return to the Project
Each time you want to work on the project, remember to activate the virtual environment for the backend:
```bash
cd /path/to/arxiv_recommender/backend
source venv/bin/activate
```

The frontend doesn't require a virtual environment, just make sure Node.js is installed on your system.



-----------------------------------------------------------------------------------------------------

# Project Proposal

#### Project Objectives

The goal of this project is to design and prototype a personalized academic paper recommender system that fetches and displays daily new machine learning papers from arXiv.org. The app will focus on helping users discover relevant research efficiently by learning from their preferences. The system will prioritize unread papers that are most likely to be of interest and organize the user’s previously read papers in a separate, easily accessible section. Automatic paper summarization will be implemented using a LLM API such as GPT-4o.

Objectives:
- Implement a pipeline to automatically fetch and display newly published machine learning papers from arXiv daily.
- Design and build an interactive user interface for browsing, reading, and rating papers.
- Develop a personalized recommendation algorithm that improves over time based on user interactions (likes, clicks, reads).
- Create a clear and user-friendly separation between "Unread Recommended Papers" and "Previously Read Papers."
- Integrate a paper summarization feature powered by GPT-4o to generate short, digestible summaries of each paper.

#### Target Users and Their Needs

**Target Users:**
- Machine learning researchers, graduate students, and practitioners who regularly read academic papers.

**User Needs:**
- A fast and easy way to keep up with newly published ML papers.
- Personalized recommendations to avoid overwhelming lists of irrelevant content.
- A simple interface to track papers they’ve already read.
- The ability to give feedback (e.g., thumbs up/down) to improve future recommendations.

#### Key Deliverables

- A functional prototype of the arXiv recommender app with:
  - Daily scraping of ML-related papers from arXiv.
  - Paper listing and detail views.
  - User login and preference tracking.
  - Recommendation algorithm that adapts based on user input.
- UI/UX designs for the app.
- A final presentation and demo video showing the system in use.
- Project report including technical details.

#### Special Constraints

- **Rate Limiting & API Use**: Must comply with arXiv’s API usage terms to avoid excessive load on their servers.
- **Privacy**: If storing any user data (e.g., preferences, read history), basic user privacy must be respected.
- **Scalability**: The prototype should be designed to support potential scaling, though full scalability is not required at this stage.
- **No Full Authentication System**: For this class prototype, user tracking may be session-based or limited to avoid complex backend implementation.

#### Expected Outcome

By the end of the project, we expect to have a working demo of a personalized research paper browsing experience. Users will be able to interact with newly published papers, receive meaningful recommendations, and have a record of their reading history. The project will demonstrate the value of UI/UX design in building efficient tools for researchers and how machine learning can enhance personalized discovery.

### Features

- **Daily ArXiv Syncing**: Automatically fetches the latest ML-related papers from arXiv.
- **Personalized Recommendations**: Learns from user feedback (likes, views) to suggest relevant unread papers.
- **GPT-4o Paper Summarization**: Summarizes paper content (e.g., abstract + intro) to help users quickly assess relevance.
- **Read History Tracking**: Separates read vs. unread papers for better paper management.
- **User Feedback System**: Allows thumbs up/down or rating interactions to fine-tune future recommendations.
- **Clean and Simple UI**: Intuitive interface with desktop and mobile-friendly layouts.

### Timeline

| Week | Milestone |
|------|-----------|
| Week 1 | Project planning, wireframes, and tech stack decisions |
| Week 2 | ArXiv scraping + initial UI prototype |
| Week 3 | User preference tracking + basic recommendation system |
| Week 4 | GPT-4o summarization integration |
| Week 5 | Read history & interaction feedback features |
| Week 6 | Polish UI, finalize features, and conduct user testing |
| Week 7 | Prepare final presentation, documentation, and demo video |

### Contact Information

- **Lead Developer & Designer:** Kyle Kim
- **Email:** kylewkim@uw.edu
- **GitHub:** [github.com/kylewskim](https://github.com/kylewskim)  
- **Client Contact:** Zeyi Chen

---
