from pydantic import BaseModel, Field
from typing import Optional, List

class Item(BaseModel):
    id: str
    note: Optional[str] = Field(default="")
    total: int

class Order(BaseModel):
    id: str = Optional[str]
    items: List[Item]
    table_number: str
    created_at: str