from django.shortcuts import render
from app.models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
class Schoollist(ListView):
    model=School
    context_object_name='allso'


class Schooldetail(DetailView):
    model=School
    context_object_name='DOSI'

class Schoolcreate(CreateView):
    model=School
    fields='__all__'

class Schoolupdate(UpdateView):
    model=School
    fields='__all__'  

class Schooldelete(DeleteView):
    model=School
    context_object_name='dso'
    success_url=reverse_lazy('Schoollist')
        

