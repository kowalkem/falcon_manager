from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views import generic
from .models import Falcon

# Views for breeding app

def index(request):
    """ Renders index page for breeding app """
    return render(request, 'index.html')

class FalconList(generic.ListView):
    """ Renders list of all falcons """
    model = Falcon

class FalconDetail(generic.DetailView):
    """ Renders info about falcon with specified id """
    model = Falcon
