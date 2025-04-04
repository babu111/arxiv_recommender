## ArXiv Paper Recommender App – Project Proposal

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
