from werkzeug.middleware.shared_data import SharedDataMiddleware
import os


class StaticFileHandler:
    def __init__(self, app, static_url='/static', static_folder='static'):
        self.app = SharedDataMiddleware(app, {
            static_url: os.path.join(os.getcwd(), static_folder)
        })

    def wsgi_app(self, environ, start_response):
        return self.app(environ, start_response)