from pydantic import BaseModel, Field
from typing import Optional

class Menu(BaseModel):
    id: str = Optional[str]
    title: str = Field(...)
    price: int = Field(...)
    description: str = Field(...)
    img: str = Field(...)