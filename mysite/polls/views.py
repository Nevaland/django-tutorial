from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, django world! You're at the polls index.")
