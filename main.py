from fastapi import FastAPI, Depends
from .request_models import UserRequest
from .database import SessionLocal
from .models import User
from sqlalchemy.orm import Session

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/user/")
async def create_user(user: UserRequest,db: Session = Depends(get_db)):
    new_user = User(type=user.type, full_name = user.full_name,username=user.full_name,email=user.email,password=user.password,submitted_by=user.submitted_by)
    db.add(new_user)
    db.commit()
    return user


