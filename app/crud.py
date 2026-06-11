from sqlalchemy.orm import Session
from sqlalchemy import or_
from datetime import datetime, timezone
from app.models import Ticket, Note
from app.schemas import TicketCreate, TicketUpdate

# Generates a unique ticket ID like TKT-001 based on total tickets in DB
def generate_ticket_id(db: Session):
    count = db.query(Ticket).count()
    return f"TKT-{str(count + 1).zfill(3)}"

# Creates a new ticket and saves it to the database
def create_ticket(db: Session, ticket: TicketCreate):
    ticket_id = generate_ticket_id(db)
    
    # Create a new Ticket object with data from the request
    new_ticket = Ticket(
        ticket_id=ticket_id,
        customer_name=ticket.customer_name,
        customer_email=ticket.customer_email,
        subject=ticket.subject,
        description=ticket.description,
        status="Open"
    )
    
    # Add to session, commit to DB, refresh to get the saved data back
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

# Fetches all tickets with optional search and status filter
def get_all_tickets(db: Session, search: str = None, status: str = None):
    query = db.query(Ticket)
    
    # If search term provided, look across name, email, ticket_id and description
    if search:
        query = query.filter(
            or_(
                Ticket.customer_name.ilike(f"%{search}%"),
                Ticket.customer_email.ilike(f"%{search}%"),
                Ticket.ticket_id.ilike(f"%{search}%"),
                Ticket.description.ilike(f"%{search}%")
            )
        )
    
    # If status filter provided, only return tickets with that status
    if status:
        query = query.filter(Ticket.status == status)
    
    return query.order_by(Ticket.created_at.desc()).all()

# Fetches a single ticket by its ticket_id including all its notes
def get_ticket(db: Session, ticket_id: str):
    return db.query(Ticket).filter(Ticket.ticket_id == ticket_id).first()

# Updates ticket status and/or adds a new note
def update_ticket(db: Session, ticket_id: str, data: TicketUpdate):
    ticket = get_ticket(db, ticket_id)
    
    # If ticket not found return None
    if not ticket:
        return None
    
    # Update status only if a new status was provided
    if data.status:
        ticket.status = data.status
    
    # Add a new note only if note text was provided
    if data.note_text:
        new_note = Note(
            ticket_id=ticket_id,
            note_text=data.note_text
        )
        db.add(new_note)
    
    # Update the updated_at timestamp
    ticket.updated_at = datetime.now(timezone.utc)
    
    db.commit()
    db.refresh(ticket)
    return ticket