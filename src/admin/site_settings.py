from flask import current_app
from ..clients import NextRevalidateClient
from .secure_model import SecureModelView


class SiteSettingsAdmin(SecureModelView):
    form_columns = ["address", "phone", "email", "hours"]
    column_list = [*form_columns, "id"]

    def on_model_change(self, form, model, is_created):
        next_client: NextRevalidateClient = current_app.next_client
        super().on_model_change(form, model, is_created)
        next_client.revalidate_tag(["site-settings"])
