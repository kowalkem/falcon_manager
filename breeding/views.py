import os, datetime
from django.conf import settings
from django.http import response
from django.views import generic
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from docx import Document
from .models import Falcon, Pair, Aviary, Office, Birth_cert
from .forms import (
    FalconCreateForm,
    FalconUpdateForm,
    PairCreateForm,
    PairUpdateForm,
    YoungFalconCreateForm,
    AviaryCreateForm,
    AviaryUpdateForm,
    OfficeCreateForm,
    OfficeUpdateForm,
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
        falcons_ids = form.data.getlist('falcons')
        falcons = [Falcon.objects.get(pk=id) for id in falcons_ids]
        res = super().form_valid(form)
        # create docx using form data and append it to form
        doc = Document(os.path.join(settings.MEDIA_ROOT, 'falcon_docs/birth_cert.docx'))
        doc.paragraphs[0].runs[1] = form.instance.document_number

        doc.tables[0].rows[1].cells[1].paragraphs[0].runs[0].text = form.instance.owner.username
        profile = form.instance.owner.user_profile
        doc.tables[0].rows[2].cells[1].paragraphs[0].runs[0].text = f'{profile.street} {profile.house_number}, {profile.zip_code} {profile.city}'


        doc.tables[1].rows[1].cells[1].paragraphs[0].runs[0].text = ''
        doc.tables[1].rows[2].cells[1].paragraphs[0].runs[0].text = ''
        species_list = [falcon.species for falcon in falcons]
        species_count = [(species.name, species.latin, species_list.count(species)) for species in set(species_list)]
        for species in species_count:
            doc.tables[1].rows[1].cells[1].paragraphs[0].runs[0].text = f'{species[1]} - {species[2]}szt.'
            doc.tables[1].rows[2].cells[1].paragraphs[0].runs[0].text = f'{species[0]} - {species[2]}szt.'

        # num females
        doc.tables[3].rows[0].cells[6].paragraphs[0].runs[0].text = f'Żeńskich: {len([falcon for falcon in falcons if falcon.sex == "F"])}'
        # num males
        doc.tables[3].rows[1].cells[0].paragraphs[0].runs[0].text = f'męskich: {len([falcon for falcon in falcons if falcon.sex == "M"])}'
        # num undefined
        doc.tables[3].rows[1].cells[2].paragraphs[0].runs[0].text = f'płci nieznanej: {len([falcon for falcon in falcons if falcon.sex == None])}'
        # num total
        doc.tables[3].rows[1].cells[4].paragraphs[0].runs[0].text = f'łącznie: {len(falcons)}'

        # birth dates
        birthdates = [falcon.birth_date for falcon in falcons]
        doc.tables[4].rows[1].cells[0].paragraphs[0].runs[0].text = f'urodzenia (wyklucia itp.): {min(birthdates)} - {max(birthdates)}'

        # vet control date
        doc.tables[4].rows[1].cells[1].paragraphs[0].runs[0].text = f'kontroli weterynaryjnej miotu: {max(birthdates) + datetime.timedelta(days=5)}'

        # list of falcons
        for i, falcon in enumerate(falcons, start=1):
            if len(doc.tables[5].rows) < i+2:
                doc.tables[5].add_row(doc.tables[5].rows[2])
            doc.tables[5].rows[i+1].cells[0].paragraphs[0].runs[0].text = str(i)
            doc.tables[5].rows[i+1].cells[1].paragraphs[0].runs[0].text = falcon.get_sex_display() if falcon.sex else 'płeć nieznana'
            doc.tables[5].rows[i+1].cells[2].paragraphs[0].runs[0].text = f'Obrączka zamknięta nr {falcon.ring}'
            doc.tables[5].rows[i+1].cells[3].paragraphs[0].runs[0].text = 'brak'

        doc.save(os.path.join(settings.MEDIA_ROOT, f'falcon_docs/{form.instance.owner.username}/birth_cert_{form.instance.document_number}.docx'))
        print(form.is_bound)
        return res

    def get_context_data(self, **kwargs):
        context = super(Birth_certCreate, self).get_context_data(**kwargs)
        context["form"].fields["vet_office"].queryset = Office.objects.filter(office_type="PIW")
        context["form"].fields["falcons"].queryset = Falcon.objects.all()
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


class OfficeList(LoginRequiredMixin, generic.ListView):

    model = Office
    paginate_by = 10

    def get_queryset(self):
        return Office.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(OfficeList, self).get_context_data(**kwargs)
        context["title"] = "List of all offices"
        return context


class OfficeDetail(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):

    model = Office

    def test_func(self):
        Office = self.get_object()
        return self.request.user == Office.owner

    def get_context_data(self, **kwargs):
        context = super(OfficeDetail, self).get_context_data(**kwargs)
        context["title"] = "Office details"
        return context


class OfficeCreate(LoginRequiredMixin, generic.edit.CreateView):
    """ View for creating new Office """

    model = Office
    form_class = OfficeCreateForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(OfficeCreate, self).get_context_data(**kwargs)
        context["title"] = "Add a new Office"
        return context


class OfficeUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.edit.UpdateView):

    model = Office
    form_class = OfficeUpdateForm

    def test_func(self):
        Office = self.get_object()
        return self.request.user == Office.owner

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(OfficeUpdate, self).get_context_data(**kwargs)
        context["title"] = "Update a Office"
        return context


class OfficeDelete(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):

    model = Office
    success_url = "/breeding/offices"

    def test_func(self):
        Office = self.get_object()
        return self.request.user == Office.owner

    def get_context_data(self, **kwargs):
        context = super(OfficeDelete, self).get_context_data(**kwargs)
        context["title"] = "Delete an Office"
        return context