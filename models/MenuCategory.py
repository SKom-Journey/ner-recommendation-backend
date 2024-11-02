from pydantic import BaseModel, Field
from typing import Optional

class MenuCategory(BaseModel):
    id: str = Optional[str]
    category_id: str = Field(...)
    menu_id: str = Field(...)
    created_at: str = Field(...)