from pydantic import BaseModel
from typing import Optional

from pydantic import BaseModel, EmailStr




class Registration(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    is_active: Optional[bool]
    is_staff: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "first_name": "Nazira",
                "last_name": "Qodirva",
                "username": "acrid",
                "email": "nazira.kodirova@mail.ru",
                "password": "*****",
                "is_active": True,
                "is_staff": True
            }
        }


class Login(BaseModel):
    username: str
    password: str