# Support CRM

A full-stack customer support ticketing system built with FastAPI, SQLite, and Tailwind CSS.

## Tech Stack
- Backend: Python 3.11 + FastAPI
- Database: SQLite + SQLAlchemy
- Frontend: HTML + Tailwind CSS + Jinja2
- Deployment: Railway.app

## Features
- Create support tickets with auto-generated IDs
- List all tickets in a clean table view
- Search across name, email, ID and description
- Filter tickets by status (Open, In Progress, Closed)
- View and update ticket details
- Add internal notes to tickets

## Setup Instructions

### Prerequisites
- Python 3.11
- uv package manager

### Run Locally
1. Clone the repo
   git clone https://github.com/ajitaiml/support-crm.git
   cd support-crm

2. Install dependencies
   uv sync

3. Run the app
   uvicorn app.main:app --reload

4. Open browser at http://127.0.0.1:8000

## API Endpoints
- POST /api/tickets - Create a new ticket
- GET /api/tickets - List all tickets with search and filter
- GET /api/tickets/{ticket_id} - Get ticket details
- PUT /api/tickets/{ticket_id} - Update ticket status and add note

## Environment Variables
Copy .env.example to .env and fill in values.
