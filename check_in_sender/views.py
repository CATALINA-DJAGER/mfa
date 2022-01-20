from django.http import HttpResponse


def index(request):
    return HttpResponse("Do you want to send some check-in?")
