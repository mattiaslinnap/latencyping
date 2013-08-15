
from collections import defaultdict
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from ping.models import Upload


@login_required
def index(request):
    uploads = list(Upload.objects.order_by('time').all())
    byname = defaultdict(list)
    for u in uploads:
        byname[u.name].append(u)
    names = sorted(byname)
    byname = [(n, byname[n]) for n in names]
    return render(request, 'ping/index.html', {'byname': byname})


@login_required
def delete(request, upload_id):
    get_object_or_404(Upload, pk=int(upload_id)).delete()
    return redirect('ping.views.index')


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
