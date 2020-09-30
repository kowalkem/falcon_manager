from django.views import generic
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Falcon, Pair
from .forms import FalconCreateForm, FalconUpdateForm, PairCreateForm, PairUpdateForm


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
    form_class = FalconCreateForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
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