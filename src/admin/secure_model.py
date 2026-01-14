import flask_login as login
from flask import url_for, redirect
from flask_admin.contrib.sqla import ModelView


class SecureModelView(ModelView):
    def is_accessible(self):
        return login.current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("admin.login_view"))
