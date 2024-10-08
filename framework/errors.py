from framework.template import HtmlResponse


def error_404(request):
    return HtmlResponse("404.html")


def error_500(request):
    return HtmlResponse("500.html")