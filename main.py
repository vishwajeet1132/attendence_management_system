from fastapi import FastAPI, Depends,HTTPException, status
from .request_models import UserRequest
from .database import SessionLocal
from .models import User
from sqlalchemy.orm import Session
from sqlalchemy import or_

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/user/")
async def create_user(user: UserRequest,db: Session = Depends(get_db)):
    user_exist = db.query(User).filter(or_(User.username == user.username, User.email == user.email)).first()
    if user_exist:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username or email already exists."
        )
    new_user = User(type=user.type, full_name=user.full_name,username=user.username,email=user.email,password=user.password,submitted_by=user.submitted_by)
    db.add(new_user)
    db.commit()
    return user


