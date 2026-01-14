from pathlib import Path
from flask import url_for
from flask_admin.form import FileUploadField
from flask_wtf.file import FileAllowed
from markupsafe import Markup
from .secure_model import SecureModelView


class ImageAdmin(SecureModelView):
    column_list = ["id", "filename", "preview"]
    form_columns = ["filename"]

    form_extra_fields = {
        "filename": FileUploadField(
            "Project Image",
            base_path=str(Path(__file__).parents[1] / "static" / "uploads"),
            validators=[
                FileAllowed(
                    ["jpg", "png", "jpeg", "JPG", "JPEG", "PNG"], "Images only!"
                )
            ],
            allow_overwrite=False,
        )
    }

    def _column_preview(self, context, model, name):
        if not model.filename:
            return ""
        img_url = url_for(
            "uploads_api.get_image", filename=model.filename, _external=True
        )
        return Markup(f'<img src="{img_url}" width="50" alt="Thumbnail">')

    column_formatters = {
        "preview": _column_preview,
    }

    column_labels = {
        "preview": "Preview",
    }
