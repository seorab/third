from django.http import HttpResponse
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt

from app.models import Address

@csrf_exempt
def save(request, id):
    address = request.POST['address']
    a = Address.objects.get(id=id)
    a.address = address
    a.save()

    return HttpResponse('ok')

def edit(request, id):
    address = Address.objects.get(id=id)
    return render(request, 'app/edit.html',
                  {'address': address})

def list(request):
    address = Address.objects.all()
    return render(
        request,
        'app/list.html',
        {'address': address}
    )

def index(request):
    address = ''
    try:
        address = request.GET['address']

        # DB insert
        add = Address(address=address)
        add.save()

    except MultiValueDictKeyError:
        pass
    return HttpResponse(
        '{"Hello": "' + address + '"}')











