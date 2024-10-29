from pydantic import BaseModel, Field
from models.Menu import Menu
from typing import Optional, List

class Chat(BaseModel):
    id: str = Optional[str]
    user_id: str = Field(...)
    user_message: str = Field(...)
    items: List[str] = Optional[list[str]]
    menus: List[Menu] = Optional[list[str]]
    created_at: str = Field(...)