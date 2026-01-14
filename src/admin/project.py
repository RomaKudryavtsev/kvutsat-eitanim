from flask import current_app
from ..clients import NextRevalidateClient
from .secure_model import SecureModelView
from .editors import QuillTextAreaField


class ProjectAdmin(SecureModelView):
    form_columns = ["name", "description", "status", "location", "images"]
    column_list = ["id", "created_at", "name", "status", "location"]

    form_overrides = {
        "description": QuillTextAreaField,
    }

    def on_model_change(self, form, model, is_created):
        next_client: NextRevalidateClient = current_app.next_client
        super().on_model_change(form, model, is_created)
        next_client.revalidate_tag([f"project-{model.id}"])
