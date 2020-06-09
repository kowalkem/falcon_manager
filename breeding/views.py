from django.views import generic
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Falcon
from .forms import FalconCreateForm, FalconUpdateForm


def index(request):
    """ Renders index page for breeding app """
    return render(request, 'index.html')


class FalconList(LoginRequiredMixin, generic.ListView):
    """ Renders list of all falcons """
    model = Falcon

    def get_queryset(self):
        return Falcon.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(FalconList, self).get_context_data(**kwargs)
        context['title'] = 'List of all falcons'
        return context


class FalconDetail(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    """ Renders info about falcon with specified id """
    model = Falcon

    def test_func(self):
        falcon = self.get_object()
        return self.request.user == falcon.owner

    def get_context_data(self, **kwargs):
        context = super(FalconDetail, self).get_context_data(**kwargs)
        context['title'] = 'Falcon details'
        return context


class FalconCreate(LoginRequiredMixin, generic.edit.CreateView):
    """ View for creating new falcon """
    model = Falcon
    form_class = FalconCreateForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(FalconCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add a new falcon'
        return context


class FalconUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.edit.UpdateView):
    """ View for updating a falcon """
    model = Falcon
    form_class = FalconUpdateForm

    def test_func(self):
        falcon = self.get_object()
        return self.request.user == falcon.owner

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(FalconUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Update a falcon'
        return context


class FalconDelete(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """ Delete a falcon with a specified id """
    model = Falcon
    success_url = '/breeding/falcons'

    def test_func(self):
        falcon = self.get_object()
        return self.request.user == falcon.owner

    def get_context_data(self, **kwargs):
        context = super(FalconDelete, self).get_context_data(**kwargs)
        context['title'] = 'Delete a falcon'
        return context
