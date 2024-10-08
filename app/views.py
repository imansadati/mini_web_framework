from framework.template import HtmlResponse


def home(request):
    return HtmlResponse("home.html")


def user_profile(request, user_id):
    context = {
        'user_id': user_id
    }
    return HtmlResponse('profile.html', context=context)