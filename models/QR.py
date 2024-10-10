from pydantic import BaseModel, Field
from typing import Optional

class QR(BaseModel):
    id: str = Optional[str]
    table_number: str = Field(...)
    is_enabled: bool = Field(default=True)