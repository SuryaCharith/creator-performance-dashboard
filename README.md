Creator Performance Dashboard (Track B)
**Track Chosen + Why**

Track B — Creator Performance Dashboard

I chose this track to demonstrate my ability to work with analytics data, build clean REST APIs, and present insights through a simple dashboard. This aligns well with my interest in data analysis and backend-driven applications.
Features Implemented

 Analytics dashboard showing key creator metrics

 Platform-based filtering (Instagram / YouTube)

 Metrics summary cards (Impressions, Engagement, Followers Gained)

 Analytics data table view

 REST APIs with validation and error handling

 SQLite database with seeded mock data

 Basic empty states and clean UI
 Tech Stack

Frontend

React (Vite)

JavaScript

Basic CSS (inline styling)

Backend

Python

FastAPI

SQLite

## How to Run Locally

### Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python seed.py
uvicorn main:app --reload



Backend runs at:

http://127.0.0.1:8000


Swagger API Docs:
http://127.0.0.1:8000/docs

Frontend

bash

cd frontend
npm install
npm run dev
Frontend runs at:
http://localhost:5173

API Endpoints
Method	Endpoint	Description
GET	/	Health check
GET	/analytics	Fetch analytics data
GET	/analytics?platform=instagram	Filter by platform
GET	/metrics	Fetch aggregated metrics
GET	/metrics?platform=youtube	Filtered metrics

Data Model
Table: analytics
Field	Type
id	Integer (Primary Key)
platform	Text
date	Text (YYYY-MM-DD)
impressions	Integer
likes	Integer
comments	Integer
followers_gained	Integer

 AI Usage Log

 How it helped
- Assisted in structuring backend APIs
- Helped with React component organization
- Suggested improvements for filtering logic

 Example Prompt
- "Create a FastAPI endpoint to filter analytics data by platform"

 Example Correction
- Initial filtering logic was inefficient
- Refactored to validate inputs and apply filtering at database query level

Trade-offs & Next Improvements

Used mock data instead of real social media APIs to reduce complexity

Limited filters to one dimension (platform) to stay within time constraints

Metrics aggregation is done on the backend for clarity

Future improvements:

Date range filtering

Charts/visualizations

Authentication and user-based dashboards

Sample Data

Mock analytics data is seeded using a Python script (seed.py) with multiple records across Instagram and YouTube to simulate real creator performance metrics.

Demo Video:

