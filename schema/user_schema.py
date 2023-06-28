from typing import Optional
from pydantic import BaseModel

class UserSchema(BaseModel):
    id: Optional[int]
    name: str
    password: str
