from pydantic import BaseModel

class UserRequest(BaseModel):
    type: str
    full_name: str
    username: str
    email: str
    password: str
    submitted_by: str

