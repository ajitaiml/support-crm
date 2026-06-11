from sqlalchemy.orm import Session
from sqlalchemy import or_
from datetime import datetime,timezone
from app.models import Ticket,Note
from app.schemas import TicketCreate,TicketUpdate

# Generate a unqiue ticket ID
def generate_ticket_id(db: Session):
    count = db.query(Ticket).count()
    return f"TKT-{str(count + 1).zfill(3)}"

# Create a new ticket and saves it to database
def create_ticket(db: Session,ticket: TicketCreate):
    ticket_id = generate_ticket_id(db)
    
    new_ticket = Ticket(
        ticket_id = ticket_id,
        customer_name = ticket.customer_name,
        customer_email = ticket.customer_email,
        subject = ticket.subject,
        description = ticket.description,
        status = "Open"
    )
    
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

# Fetch all  tickets with optional search and status filer
def get_all_tickets(db: Session, search: str = None, status: str = None):
    query = db.query(Ticket)
    
    # Search Term provided
    if search:
        query = query.filter(
            or_(
                Ticket.customer_name.ilike(f"%{search}%"),
                Ticket.customer_email.ilike(f"%{search}%"),
                Ticket.ticket_id.ilike(f"%{search}%"),
                Ticket.ticket_id.ilike(f"%{search}%")
            )
        )
        
    # Filter Term Provided
    if status:
        query = query.filter(Ticket.status == status)
    
    return query.order_by(Ticket.created_at.desc()).all()

# Fetch a single ticket by ticket_id 
def get_ticket(db: Session, ticket_id: str):
    return db.query(Ticket).filter(Ticket.ticket_id == ticket_id).first()

# Update ticket status and/or adds a new note
def update_ticket(db: Session, ticket_id: str, data: TicketUpdate):
    ticket = get_ticket(db, ticket_id)
    
    # Ticket not found
    if not ticket:
        return None
    
    # Update status only if a new status was provided
    if data.status:
        ticket.status = data.status
        
    # Add new note when note text is provided
    if data.note_text:
        new_note = Note(
            ticket_id = ticket_id,
            note_text = data.note_text
        )
        db.add(new_note)
        
    ticket.updated_at = datetime.now(timezone.utc)
    
    db.commit()
    db.refresh(ticket)
    return ticket