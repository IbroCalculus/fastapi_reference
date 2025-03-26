from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    Hashed_password: str
