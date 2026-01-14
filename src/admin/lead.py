from .secure_model import SecureModelView


class LeadAdmin(SecureModelView):
    can_delete = False
    can_create = False

    form_columns = ["name", "email", "phone", "message"]
    column_list = ["id", "created_at", "name", "email", "phone", "message"]
