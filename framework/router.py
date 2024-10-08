from werkzeug.routing import Map, Rule


class Router:
    def __init__(self):
        self.url_map = Map()

    def add_route(self, path, handler, methods=['GET']):
        rule = Rule(path, endpoint=handler, methods=methods)
        self.url_map.add(rule)

    def dispatch(self, request):
        urls = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, args = urls.match()
            return endpoint, args
        except Exception as e:
            return None, {}