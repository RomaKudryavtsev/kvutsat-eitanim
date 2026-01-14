from flask import current_app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, ValidationError
from ..services import UserService


class AdminLoginForm(FlaskForm):
    login = StringField("Login", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

    def validate_login(self, field):
        user = self.get_user()
        if user is None:
            raise ValidationError("Invalid user")
        if not user.check_password(self.password.data):
            raise ValidationError("Invalid password")

    def get_user(self):
        user_service: UserService = current_app.user_service
        return user_service.get_user_by_username(username=self.login.data)
