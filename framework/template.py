import os
from jinja2 import FileSystemLoader, Environment
from werkzeug.wrappers import Response


class HtmlResponse(Response):
    def __init__(self, template_name, templates_dir="templates", context=None):
        if context is None:
            context = {}

        self.templates_env = Environment(
            loader=FileSystemLoader(os.path.abspath(templates_dir)))
        text = self.templates_env.get_template(template_name).render(**context)

        super(HtmlResponse, self).__init__(text, content_type="text/html")