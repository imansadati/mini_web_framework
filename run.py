from app.urls import app
from framework.static import StaticFileHandler
from framework.middleware import Middleware
from werkzeug.serving import run_simple


class LoggingMiddleware(Middleware):
    def process_request(self, request):
        print(f'Request received: {request.method} {request.path}')
        return request

    def process_response(self, request, response):
        print(f"Response: {response.status}")
        return response


app.add_middleware(LoggingMiddleware())

if __name__ == '__main__':
    app = StaticFileHandler(app).wsgi_app
    run_simple('127.0.0.1', 8000, app, use_debugger=True)