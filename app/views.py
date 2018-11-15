from django.http import HttpResponse
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

from app.models import Address


def list(request):
    address = Address.objects.all()
    return HttpResponse(address)

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











