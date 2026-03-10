from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    hashed_password: str
    is_active: bool = True
    created_at: datetime = datetime.utcnow()