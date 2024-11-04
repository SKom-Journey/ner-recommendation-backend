from pydantic import BaseModel, Field
from typing import Optional

class Admin(BaseModel):
    id: str = Optional[str]
    username: str = Field(...)
    password: str = Field(...)
    created_at: str