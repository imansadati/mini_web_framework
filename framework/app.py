from werkzeug.wrappers import Request
from framework.router import Router
from framework.errors import error_404, error_500


class MiniFramework:
    def __init__(self):
        self.router = Router()
        self.middlewares = []

    def route(self, path, methods=['GET']):
        def wrapper(handler):
            self.router.add_route(path, handler, methods)
            return handler
        return wrapper

    def add_middleware(self, middleware):
        self.middlewares.append(middleware)

    def wsgi_app(self, environ, start_response):
        request = Request(environ)

        try:
            handler, kwargs = self.router.dispatch(request)
            if handler is None:
                response = error_404(request)
            else:
                for middleware in self.middlewares:
                    request = middleware.process_request(request)

                response = handler(request, **kwargs)

                for middleware in reversed(self.middlewares):
                    response = middleware.process_response(request, response)
        except Exception as e:
            print(e)
            response = error_500(request)

        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)