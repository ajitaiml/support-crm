from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List,Optional
from app.database import get_db
from app.schemas import TicketCreate,TicketList,TicketUpdate,TicketRead
from app import crud

router = APIRouter(prefix="/api/tickets",tags=["tickets"])


@router.post("/")
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    new_ticket = crud.create_ticket_db(db,ticket)
    return {
        "ticket_id": new_ticket.ticket_id,
        "created_at": new_ticket.created_at
    }
    
    
@router.get("/", response_model= List[TicketList])
def get_all_tickets(
    search: Optional[str] =  None,
    status: Optional[str] = None,
    db: Session = Depends(get_db)
):
    tickets = crud.get_all_tickets(db, search=search, status=status)
    return tickets


@router.get("/{ticket_id}", response_model=TicketRead)
def get_ticket(ticket_id: str, db: Session = Depends(get_db)):
    ticket = crud.get_ticket(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


@router.put("/{ticket_id}")
def update_ticket(ticket_id: str, data: TicketUpdate, db: Session = Depends(get_db)):
    ticket = crud.update_ticket(db, ticket_id, data)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {
        "success": True,
        "updated_at": ticket.updated_at
    }