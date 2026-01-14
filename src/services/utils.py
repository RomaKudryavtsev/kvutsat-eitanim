from functools import wraps
from ..models import db_conn


def transactional(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            db_conn.session.commit()
            return result
        except Exception as e:
            db_conn.session.rollback()
            raise e

    return wrapper
