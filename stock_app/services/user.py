from ..repositories.user_repository import UserRepository
from ..schemas.user import UserRequest


class UserService:
    def new_user(self, user_repository: UserRepository, user: UserRequest):
        user_saved = user_repository.save(user)
        return user_saved
