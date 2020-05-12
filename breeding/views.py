from django.shortcuts import render
from django.http import HttpResponse

# Views for breeding app

def index(request):
    """ Renders index page for breeding app """
    return HttpResponse('Breeding site\'s index page')