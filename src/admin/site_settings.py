from .secure_model import SecureModelView


class SiteSettingsAdmin(SecureModelView):
    form_columns = ["title", "description", "phone", "email"]
    column_list = [*form_columns, "id"]
