import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.database import engine
from app.models import Base
from app.routers import tickets

# Create /data directory if it doesn't exist (needed for Railway volume)
os.makedirs("/data", exist_ok=True)

# Create all database tables on startup if they dont exist yet
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app
app = FastAPI(title="Support CRM")

# Tell FastAPI where the HTML templates are located
templates = Jinja2Templates(directory="templates")

# Mount the static folder only if it exists
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

# Register the tickets router - all /api/tickets endpoints are now active
app.include_router(tickets.router)


# Home page - renders the ticket list page
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "index.html")


# Create ticket page - renders the create ticket form
@app.get("/create")
def create_page(request: Request):
    return templates.TemplateResponse(request, "create.html")


# Ticket detail page - renders the detail page for a specific ticket
@app.get("/ticket/{ticket_id}")
def detail_page(request: Request, ticket_id: str):
    return templates.TemplateResponse(
        request,
        "detail.html",
        {"ticket_id": ticket_id}
    )