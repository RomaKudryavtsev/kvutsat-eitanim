from sqlalchemy import select, exists
from ..models import db_conn, User


class UserRepo:
    def get_user_by_username(self, username: str) -> User | None:
        statement = select(User).where(User.username == username)
        result = db_conn.session.execute(statement).scalar()
        return result

    def check_if_admin_exists(self, admin_username: str) -> bool:
        statement = select(exists().where(User.username == admin_username))
        result = db_conn.session.execute(statement).scalar()
        return result

    # IMPORTANT: Transactions are managed on the service layer
    def save_admin(self, admin_username: str, admin_password: str) -> User:
        new_admin = User(username=admin_username)
        new_admin.set_password(admin_password)
        db_conn.session.add(new_admin)
        db_conn.session.flush()
        db_conn.session.refresh(new_admin)
        return new_admin
