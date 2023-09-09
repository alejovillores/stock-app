from sqlalchemy.orm import Session
from ..schemas.user import UserRequest
from ..models.user import User
from ..config import log

logging = log.get_logger(__name__)


class UserRepository:
    def __init__(self, db: Session):
        self.connection = db

    def save(self, user_request: UserRequest) -> User:
        user = (
            self.connection.query(User).filter(User.email == user_request.email).first()
        )

        if user:
            logging.info("update user")
            user.name = user_request.name
            user.last_name = user_request.last_name
            user.email = user_request.email
        else:
            logging.info("new user")
            user = User(**user_request.dict())
            self.connection.add(user)

        self.connection.commit()
        return user
