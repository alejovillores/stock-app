from sqlalchemy.orm import Session
from ..schemas.user import UserRequest
from ..models.user import User


class UserRepository:
    def __init__(self, db: Session):
        self.connection = db

    def save(self, user_request: UserRequest) -> User:
        user = (
            self.connection.query(User).filter(User.email == user_request.email).first()
        )

        if user:
            user.name = user_request.name
            user.last_name = user_request.last_name
            user.email = user_request.email
        else:
            user = User(
                name=user_request.name,
                last_name=user_request.last_name,
                email=user_request.email,
                password=user_request.password,
            )
            self.connection.add(user)

        self.connection.commit()
        return user
