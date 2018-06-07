from django.shortcuts import render
from django.views.generic import CreateView, FormView, ListView, DetailView, UpdateView
from django.db.models import *
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

# Create your views here.

def home (request):
    form = CableForm(request.POST or None)

    return render(request,"cable.html",{form: form})

class CreateCableModel(CreateView):
    model = Cable
    fields = ['']
    success_url = '/'

class CreateDeviceModel(CreateView):
    model = Device
    fields = ['']
    success_url = '/device/'

def add_cable(request):
    if request.method=='POST':
        pass
    redirect('cable_list')

