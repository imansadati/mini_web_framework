class Middleware:
    def process_request(self, request):
        return request

    def process_response(self, request, response):
        return response