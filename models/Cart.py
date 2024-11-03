from pydantic import BaseModel, Field
from typing import Optional
from models.Menu import Menu

class Cart(BaseModel):
    id: str = Optional[str]
    user_id: str = Field(...)
    menu_id: str = Field(...)
    quantity: int = Field(...)
    note: str = Field(...)
    created_at: str = Field(...)

    menu: Menu = Optional[Menu]