from pydantic import BaseModel, Field
from typing import Optional, List

class Menu(BaseModel):
    id: str = Optional[str]
    title: str = Field(...)
    price: int = Field(...)
    description: str = Field(...)
    img: str = Field(...)

class MenuList(BaseModel):
    category_name: str = Field(...)
    items: List[Menu]
    