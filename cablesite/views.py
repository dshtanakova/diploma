from django.shortcuts import render
from django.views.generic import CreateView, FormView, ListView, DetailView, UpdateView
from django.db.models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.forms.models import modelformset_factory
from django.contrib import messages
from .models import *
from django.http import *
from .forms import *

# Create your views here.

def home (request):
    data = {'message': 'hi there'}
    return render(request, "home.html", context=data)

def cable_view(request):

    cable = Cable.objects.all()
    return render(request, "cable.html", {'cable': cable})

def panel_view(request):
    return render(request, 'panel.html',{'panel': Panel.objects.all()})

class HomePageView(TemplateView):
    template_name = 'demo/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'hello http://example.com')
        return context


class CreateCableModel(CreateView):
    model = Cable
    fields = ['']
    success_url = '/'

class CreateDeviceModel(CreateView):
    model = Device
    fields = ['']
    success_url = '/device/'

def add_cable(request):
    if request.method == "POST":
        cab = Cable()
        cab.cable_mark = request.POST.get("cable mark")
        cab.destination_to = request.POST.get("destination to")
        cab.destination_from = request.POST.get('destination from')
        cab.status = request.POST.get('status')
        cab.cross_section = request.POST.get('cross section')
        cab.lenght = request.POST.get('length')
        cab.save()
    return HttpResponseRedirect("/")


def manage_cables(request):
    CableFormSet = modelformset_factory(Cable)
    if request.method == 'POST':
        formset = CableFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()

    else:
        formset = CableFormSet()
    return render("cable.html", {"formset": formset})


def m304(request):
    return HttpResponseNotModified()

def m400(request):
    return HttpResponseBadRequest("<h2>Bad Request</h2>")

def m403(request):
    return HttpResponseForbidden("<h2>Forbidden</h2>")

def m404(request):
    return HttpResponseNotFound("<h2>Not Found</h2>")

def m405(request):
    return HttpResponseNotAllowed("<h2>Method is not allowed</h2>")

def m410(request):
    return HttpResponseGone("<h2>Content is no longer here</h2>")

def m500(request):
    return HttpResponseServerError("<h2>Something is wrong</h2>")