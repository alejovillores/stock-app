from fastapi import FastAPI, status, Depends, HTTPException
from sqlalchemy.orm import Session

from .lib.version import Version
from .config.database import get_session
from .schemas import user
from .services.user import UserService
from .repositories.user_repository import UserRepository

app = FastAPI()


async def get_db():
    LocalSession = get_session()
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()


@app.get("/", status_code=status.HTTP_200_OK)
async def read_root():
    return {"status": status.HTTP_200_OK, "version": Version().current()}


@app.post(
    "/users", status_code=status.HTTP_201_CREATED, response_model=user.UserResponse
)
async def create_new_user(user: user.UserRequest, db: Session = Depends(get_db)):
    try:
        user_repository = UserRepository(db)
        user_service = UserService()
        user_created = user_service.new_user(user_repository, user)
        return user_created
    except Exception as error:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, **error.__dict__)
