from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.database import engine
from app.models import Base
from app.routers import tickets

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Support CRM")
templates = Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory="static"),name="static")
app.include_router(tickets.router)

# Home Page
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Create ticket page 
@app.get("/create")
def create_page(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})


# Ticket detail page 
@app.get("/ticket/{ticket_id}")
def detail_page(request: Request, ticket_id: str):
    return templates.TemplateResponse(
        "detail.html",
        {"request": request, "ticket_id": ticket_id}
    )