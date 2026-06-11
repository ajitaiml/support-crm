from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional,List


# Schema to create new note
class NoteCreate(BaseModel):
    note_text : str
    
# Schema to Read a note
class NoteRead(BaseModel):
    id: int
    ticket_id: str
    note_text: str
    created_at: datetime
    
    class Config:
        from_attributes = True
    
    
# Schema to create a new ticket
class TicketCreate(BaseModel):
    customer_name: str
    customer_email: EmailStr
    subject: str
    description: str
    
    
# Schema to update a ticket
class UpdateTicket(BaseModel):
    status: Optional[str] = None
    note_text: Optional[str] = None
    
    
# Schema to read a ticket in ticket list view
class TicketList(BaseModel):
    ticket_id: str
    customer_name: str
    subject: str
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True
    
# Schema for reading full ticket details including all notes
class TicketRead(BaseModel):
    ticket_id: str
    customer_name: str
    customer_email: str
    subject: str
    description: str
    status: str
    created_at: datetime
    updated_at: datetime
    notes: List[NoteRead] = []
    
    class Config:
        from_attributes = True