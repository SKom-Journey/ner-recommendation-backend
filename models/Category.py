from pydantic import BaseModel, Field
from typing import Optional

class Category(BaseModel):
    id: str = Optional[str]
    name: str = Field(...)
    created_at: str = Field(...)