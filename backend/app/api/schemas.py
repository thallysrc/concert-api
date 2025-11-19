from typing import Optional

from pydantic import BaseModel

class Concert(BaseModel):
    id: Optional[int] = None
    name: str
    date: str
    image_url: str
    location: str
    description: str | None = None
    price: float | None = None
    participants: int | None = None