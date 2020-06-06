from django.views import generic
from django.shortcuts import render
from django.contrib.auth.mixins import
from .models import Falcon
from .forms import FalconCreateForm


def index(request):
    """ Renders index page for breeding app """
    return render(request, 'index.html')


class FalconList(generic.ListView):
    """ Renders list of all falcons """
    model = Falcon

    def get_context_data(self, **kwargs):
        context = super(FalconList, self).get_context_data(**kwargs)
        context['title'] = 'List of all falcons'
        return context


class FalconDetail(generic.DetailView):
    """ Renders info about falcon with specified id """
    model = Falcon

    def get_context_data(self, **kwargs):
        context = super(FalconDetail, self).get_context_data(**kwargs)
        context['title'] = 'Falcon details'
        return context


class FalconCreate(generic.edit.CreateView):
    """ View for creating new falcon """
    model = Falcon
    form_class = FalconCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(FalconCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add a new falcon'
        return context
