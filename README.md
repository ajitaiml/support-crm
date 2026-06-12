# Support CRM

A full-stack customer support ticketing system built with FastAPI, SQLite, and HTML + Tailwind CSS.

## Live Demo

https://support-crm-production-13e4.up.railway.app

## Features

- Create support tickets with customer info, subject and description
- Auto-generated ticket IDs (TKT-001, TKT-002...)
- List all tickets with clean table view
- Search across customer name, email, ticket ID and description
- Filter tickets by status (Open, In Progress, Closed)
- View full ticket details
- Update ticket status
- Add internal notes to tickets

## Tech Stack

- **Backend:** Python 3.11, FastAPI
- **Database:** SQLite via SQLAlchemy
- **Frontend:** HTML, Tailwind CSS, Vanilla JavaScript
- **Deployment:** Railway.app

## Project Structure

```
support-crm/
├── app/
│   ├── main.py         # FastAPI app entry point
│   ├── database.py     # Database connection setup
│   ├── models.py       # Database table models
│   ├── schemas.py      # Pydantic request/response schemas
│   ├── crud.py         # Database operations
│   └── routers/
│       └── tickets.py  # API route handlers
├── templates/
│   ├── base.html       # Base layout
│   ├── index.html      # Home page - ticket list
│   ├── create.html     # Create ticket form
│   └── detail.html     # Ticket detail and update
├── static/
├── Procfile
├── requirements.txt
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/tickets/ | Create a new ticket |
| GET | /api/tickets/ | Get all tickets (supports search and filter) |
| GET | /api/tickets/{ticket_id} | Get full ticket details |
| PUT | /api/tickets/{ticket_id} | Update status and add note |

## Local Setup

### Prerequisites
- Python 3.11
- uv package manager

### Steps

1. Clone the repository
```
git clone https://github.com/ajitaiml/support-crm.git
cd support-crm
```

2. Install dependencies
```
uv sync
```

3. Run the app
```
uvicorn app.main:app --reload
```

4. Open browser at
```
http://127.0.0.1:8000
```

## Environment Variables

See `.env.example` for reference.

```
DATABASE_URL=sqlite:///./crm.db
```

## Deployment

Deployed on Railway.app with a persistent volume mounted at `/data` for SQLite storage.
