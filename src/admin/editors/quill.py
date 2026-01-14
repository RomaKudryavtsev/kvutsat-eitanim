from wtforms import TextAreaField
from wtforms.widgets import TextArea
from markupsafe import Markup


class QuillAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        kwargs.setdefault("class", "quill-editor")
        textarea_html = super().__call__(field, **kwargs)
        script = Markup(
            f"""
        <!-- Quill CDN -->
        <script src="https://cdn.jsdelivr.net/npm/quill@2.0.3/dist/quill.js"></script>
        <link href="https://cdn.jsdelivr.net/npm/quill@2.0.3/dist/quill.snow.css" rel="stylesheet">
        <style>
            .quill-editor-container {{
                min-height: 300px;
                direction: rtl;
                background-color: white;
            }}
            .quill-editor-container .ql-editor {{
                min-height: 250px;
                text-align: right;
                direction: rtl;
                background-color: white;
            }}
            .quill-editor-container .ql-editor.ql-blank::before {{
                text-align: right;
                right: 15px;
                left: auto;
            }}
        </style>
        <script>
        document.addEventListener("DOMContentLoaded", function() {{
            var container = document.createElement('div');
            container.id = '{field.id}_quill';
            container.className = 'quill-editor-container';
            var textarea = document.querySelector("#{field.id}");
            textarea.style.display = 'none';
            textarea.parentNode.insertBefore(container, textarea.nextSibling);

            var quill = new Quill('#{field.id}_quill', {{
                theme: 'snow',
                modules: {{
                    toolbar: [
                        ['bold', 'italic', 'underline', 'strike'],
                        ['link'],
                        [{{ 'list': 'bullet' }}],
                        ['clean']
                    ]
                }},
                placeholder: 'כתבו כאן...',
                bounds: '#{field.id}_quill'
            }});

            // Set initial value
            quill.root.innerHTML = textarea.value;

            // Update textarea on change
            quill.on('text-change', function() {{
                textarea.value = quill.root.innerHTML;
                textarea.dispatchEvent(new Event('input', {{ bubbles: true }}));
            }});

            // Set default direction to RTL (Hebrew content)
            container.style.direction = 'rtl';
            quill.root.style.direction = 'rtl';
            quill.root.setAttribute('dir', 'rtl');
            var range = quill.getSelection();
            if (range) {{
                quill.format('direction', 'rtl');
            }}
        }});
        </script>
        """
        )
        return textarea_html + script


class QuillTextAreaField(TextAreaField):
    widget = QuillAreaWidget()
