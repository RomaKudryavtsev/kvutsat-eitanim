from wtforms import TextAreaField
from wtforms.widgets import TextArea
from markupsafe import Markup


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        kwargs.setdefault("class", "ckeditor")
        kwargs.setdefault("dir", "rtl")
        textarea_html = super().__call__(field, **kwargs)
        script = Markup(
            f"""
        <script src="https://cdn.ckeditor.com/ckeditor5/39.0.1/classic/ckeditor.js"></script>
        <script>
        document.addEventListener("DOMContentLoaded", function() {{
            let editorElement = document.querySelector("#{field.id}");
            if (editorElement) {{
                editorElement.setAttribute('readonly', 'readonly');
                editorElement.setAttribute('dir', 'rtl');
                ClassicEditor
                    .create(editorElement, {{
                        toolbar: [
                            'heading', '|', 'bold', 'italic', 'link', 'bulletedList', 'numberedList',
                            'blockQuote', 'insertTable', 'undo', 'redo', 'imageUpload', 'direction'
                        ],
                        language: 'he'
                    }})
                    .then(editor => {{
                        editor.plugins.get('FileRepository').createUploadAdapter = (loader) => {{
                            return new UploadAdapter(loader);
                        }};
                        editor.model.document.on('change:data', () => {{
                            editorElement.value = editor.getData();
                            editorElement.dispatchEvent(new Event('input', {{ bubbles: true }}));
                        }});
                    }})
                    .catch(error => console.error("CKEditor initialization failed:", error));
            }}
        }});

        class UploadAdapter {{
            constructor(loader) {{
                this.loader = loader;
            }}
            upload() {{
                return this.loader.file.then(file => {{
                    const data = new FormData();
                    data.append('upload', file);
                    return fetch('/api/uploads/img', {{
                        method: 'POST',
                        body: data
                    }})
                    .then(response => response.json())
                    .then(result => {{
                        return {{
                            default: result.url
                        }};
                    }});
                }});
            }}
            abort() {{}}
        }}
        </script>
        """
        )
        return textarea_html + script


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()
