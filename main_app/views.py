from django.shortcuts import render
from django.http import HttpRequest
#from django.views import ListView
from django.template import RequestContext
from datetime import datetime

from.models import Blood_Request


def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'home.html',

    )


def about(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'about.html',

    )


def blood(request):

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'blood.html',

    )


def blog(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'blog.html',

    )


def contact(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'contact.html',

    )


def sign(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'sign.html',

    )





