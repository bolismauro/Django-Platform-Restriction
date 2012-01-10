from django.http import HttpResponse
from django_platform_restriction import require_platform, require_iOS

#@require_platform(['iPhone'], redirect_to = "example.views.not_allowed_home")
@require_iOS
def home(request):
    return HttpResponse("You are allowed to see this page");


def not_allowed_home(request):
    return HttpResponse("Sorry, change device or browser :D"); 