
from collections import defaultdict
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from ping.models import Upload


def index(request):
    uploads = list(Upload.objects.order_by('time').all())
    byname = defaultdict(list)
    for u in uploads:
        byname[u.name].append(u)
    names = sorted(byname)
    byname = [(n, byname[n]) for n in names]
    return render(request, 'ping/index.html', {'byname': byname})


def ping(request, size):
    size = int(size)
    assert size > 0
    return HttpResponse('a' * size)

@csrf_exempt
def upload(request, name):
    assert name
    assert request.body
    Upload.objects.create(name=name, content=request.body)
    return HttpResponse('OK')
