from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from hash import Hash


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        hashed_password=Hash.hash_password(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
