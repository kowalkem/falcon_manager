from django.views import generic
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Falcon, Pair, Aviary, Birth_cert
from .forms import (
    FalconCreateForm,
    FalconUpdateForm,
    PairCreateForm,
    PairUpdateForm,
    YoungFalconCreateForm,
    AviaryCreateForm,
    AviaryUpdateForm,
    Birth_certCreateForm,
)


def index(request):
    """ Renders index page for breeding app """
    return render(request, "index.html")


class FalconList(LoginRequiredMixin, generic.ListView):
    """ Renders list of all falcons """

    model = Falcon
    paginate_by = 10

    def get_queryset(self):
        return Falcon.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(FalconList, self).get_context_data(**kwargs)
        context["title"] = "List of all falcons"
        return context


class FalconDetail(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    """ Renders info about falcon with specified id """

    model = Falcon

    def test_func(self):
        falcon = self.get_object()
        return self.request.user == falcon.owner

    def get_context_data(self, **kwargs):
        context = super(FalconDetail, self).get_context_data(**kwargs)
        context["title"] = "Falcon details"
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
        context["title"] = "Add a new falcon"
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
        context["title"] = "Update a falcon"
        return context


class FalconDelete(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """ Delete a falcon with a specified id """

    model = Falcon
    success_url = "/breeding/falcons"

    def test_func(self):
        falcon = self.get_object()
        return self.request.user == falcon.owner

    def get_context_data(self, **kwargs):
        context = super(FalconDelete, self).get_context_data(**kwargs)
        context["title"] = "Delete a falcon"
        return context


class YoungFalconCreate(LoginRequiredMixin, generic.edit.CreateView):
    """ View for creating new falcon from pair """

    model = Falcon
    form_class = YoungFalconCreateForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        pair = Pair.objects.get(pk=self.kwargs["pair_pk"])
        form.instance.father = Falcon.objects.get(pk=pair.male.id)
        form.instance.mother = Falcon.objects.get(pk=pair.female.id)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(YoungFalconCreate, self).get_context_data(**kwargs)
        context["title"] = "Add a new falcon from specified pair"
        return context


class PairList(LoginRequiredMixin, generic.ListView):
    """ Renders list of all pairs """

    model = Pair
    paginate_by = 10

    def get_queryset(self):
        return Pair.objects.filter(
            male__owner=self.request.user, female__owner=self.request.user
        )

    def get_context_data(self, **kwargs):
        context = super(PairList, self).get_context_data(**kwargs)
        context["title"] = "List of all pairs"
        return context


class PairDetail(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    """ Renders info about pair with specified id """

    model = Pair

    def test_func(self):
        pair = self.get_object()
        return self.request.user == pair.male.owner and pair.female.owner

    def get_context_data(self, **kwargs):
        context = super(PairDetail, self).get_context_data(**kwargs)
        context["title"] = "Pair details"
        return context


class PairCreate(LoginRequiredMixin, generic.edit.CreateView):
    """ View for creating new pair """

    model = Pair
    form_class = PairCreateForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PairCreate, self).get_context_data(**kwargs)
        context["form"].fields["male"].queryset = Falcon.objects.filter(sex="M")
        context["form"].fields["female"].queryset = Falcon.objects.filter(sex="F")
        context["title"] = "Add a new pair"
        return context


class PairUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.edit.UpdateView):
    """ View for updating a pair """

    model = Pair
    form_class = PairUpdateForm

    def test_func(self):
        pair = self.get_object()
        return self.request.user == pair.male.owner and pair.female.owner

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PairUpdate, self).get_context_data(**kwargs)
        context["title"] = "Update a pair"
        return context


class PairDelete(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """ Delete a pair with a specified id """

    model = Pair
    success_url = "/breeding/pairs"

    def test_func(self):
        pair = self.get_object()
        return self.request.user == pair.male.owner and pair.female.owner

    def get_context_data(self, **kwargs):
        context = super(PairDelete, self).get_context_data(**kwargs)
        context["title"] = "Delete a pair"
        return context


class AviaryList(LoginRequiredMixin, generic.ListView):
    """ Renders list of all aviaries """

    model = Aviary
    paginate_by = 10

    def get_queryset(self):
        return Aviary.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(AviaryList, self).get_context_data(**kwargs)
        context["title"] = "List of all aviaries"
        return context


class AviaryDetail(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    """ Renders info about aviary with specified id """

    model = Aviary

    def test_func(self):
        Aviary = self.get_object()
        return self.request.user == Aviary.owner

    def get_context_data(self, **kwargs):
        context = super(AviaryDetail, self).get_context_data(**kwargs)
        context["title"] = "Aviary details"
        return context


class AviaryCreate(LoginRequiredMixin, generic.edit.CreateView):
    """ View for creating new Aviary """

    model = Aviary
    form_class = AviaryCreateForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AviaryCreate, self).get_context_data(**kwargs)
        context["title"] = "Add a new aviary"
        return context


class AviaryUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.edit.UpdateView):
    """ View for updating a aviary """

    model = Aviary
    form_class = AviaryUpdateForm

    def test_func(self):
        Aviary = self.get_object()
        return self.request.user == Aviary.owner

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AviaryUpdate, self).get_context_data(**kwargs)
        context["title"] = "Update a Aviary"
        return context


class AviaryDelete(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """ Delete an aviary with a specified id """

    model = Aviary
    success_url = "/breeding/aviaries"

    def test_func(self):
        Aviary = self.get_object()
        return self.request.user == Aviary.owner

    def get_context_data(self, **kwargs):
        context = super(AviaryDelete, self).get_context_data(**kwargs)
        context["title"] = "Delete a Aviary"
        return context


class Docs(LoginRequiredMixin, TemplateView):
    template_name = "breeding/docs.html"


class Birth_certCreate(LoginRequiredMixin, generic.edit.CreateView):

    model = Birth_cert
    form_class = Birth_certCreateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Birth_certCreate, self).get_context_data(**kwargs)
        context["title"] = "Add a new birth_cert"
        return context


class Birth_certDetail(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):

    model = Birth_cert

    def test_func(self):
        Birth_cert = self.get_object()
        return self.request.user == Birth_cert.owner

    def get_context_data(self, **kwargs):
        context = super(Birth_certDetail, self).get_context_data(**kwargs)
        context["title"] = "Birth_cert details"
        return context