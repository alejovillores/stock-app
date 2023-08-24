from pydantic import BaseModel


class UserRequest(BaseModel):
    name: str
    last_name: str
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    last_name: str
    email: str
    password: str

    class Config:
        from_attributes = True
