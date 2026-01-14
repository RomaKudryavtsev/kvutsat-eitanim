from .secure_model import SecureModelView
from .editors import CKTextAreaField, QuillTextAreaField

EDITOR = "quill"


class ArticleAdmin(SecureModelView):
    form_columns = ["title", "content"]
    column_list = ["id", "created_at", "title"]

    form_overrides = {
        "content": QuillTextAreaField if EDITOR == "quill" else CKTextAreaField
    }
