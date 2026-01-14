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
        <script src="https://cdn.jsdelivr.net/npm/quill-resize-module@2.0.4/dist/resize.min.js"></script>
        <link href="https://cdn.jsdelivr.net/npm/quill-resize-module@2.0.4/dist/resize.min.css" rel="stylesheet">
        <script>
        document.addEventListener("DOMContentLoaded", function() {{
            var container = document.createElement('div');
            container.id = '{field.id}_quill';
            container.style.direction = 'rtl';
            var textarea = document.querySelector("#{field.id}");
            textarea.style.display = 'none';
            textarea.parentNode.insertBefore(container, textarea.nextSibling);
            
            var quill = new Quill('#{field.id}_quill', {{
                theme: 'snow',
                modules: {{
                    toolbar: [
                        ['bold', 'italic', 'underline', 'strike'],
                        ['blockquote', 'code-block'],
                        ['link', 'image', 'video'],
                        [{{ 'list': 'ordered' }}, {{ 'list': 'bullet' }}],
                        [{{ 'direction': 'rtl' }}, {{ 'align': [] }}],
                        ['clean']
                    ],
                    resize: {{ modules: ['Resize', 'DisplaySize', 'Toolbar'] }}
                }},
                placeholder: 'כתוב כאן...',
                bounds: '#{field.id}_quill',
                direction: 'rtl'
            }});

            // Set initial value
            quill.root.innerHTML = textarea.value;

            // Update textarea on change
            quill.on('text-change', function() {{
                textarea.value = quill.root.innerHTML;
                textarea.dispatchEvent(new Event('input', {{ bubbles: true }}));
            }});

            // Optional: Custom image upload handler
            quill.getModule('toolbar').addHandler('image', function() {{
                var input = document.createElement('input');
                input.setAttribute('type', 'file');
                input.setAttribute('accept', 'image/*');
                input.click();
                input.onchange = function() {{
                    var file = input.files[0];
                    var formData = new FormData();
                    formData.append('upload', file);
                    fetch('/api/uploads/img', {{
                        method: 'POST',
                        body: formData
                    }})
                    .then(response => response.json())
                    .then(result => {{
                        var range = quill.getSelection();
                        quill.insertEmbed(range.index, 'image', result.url);
                    }});
                }};
            }});
        }});
        </script>
        """
        )
        return textarea_html + script


class QuillTextAreaField(TextAreaField):
    widget = QuillAreaWidget()
