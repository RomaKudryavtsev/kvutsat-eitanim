from ..models import User
from ..repos import UserRepo
from .utils import transactional


class UserService:
    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo

    def get_user_by_username(self, username: str) -> User | None:
        return self.user_repo.get_user_by_username(username)

    def check_if_admin_exists(self, admin_username: str) -> bool:
        return self.user_repo.check_if_admin_exists(admin_username)

    @transactional
    def save_admin(self, admin_username: str, admin_password: str) -> User | None:
        if self.check_if_admin_exists(admin_username):
            return None
        else:
            return self.user_repo.save_admin(admin_username, admin_password)
