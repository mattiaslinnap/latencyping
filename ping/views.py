# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse('Hello world!')


@csrf_exempt
def ping(request, size):
    size = int(size)
    assert size > 0
    return HttpResponse('a' * size)

