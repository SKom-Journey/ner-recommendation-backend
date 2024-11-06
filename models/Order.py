from pydantic import BaseModel, Field
from typing import Optional, List
from models.Menu import Menu

class Item(BaseModel):
    id: str
    name: Optional[str] = Field(default="")
    note: Optional[str] = Field(default="")
    total: int
    price: int
    detail: Optional[Menu] = Field(default=None)

class Order(BaseModel):
    id: str = Optional[str]
    items: List[Item]
    is_finished: bool
    user_id: str
    user_name: str
    table_number: str
    created_at: str