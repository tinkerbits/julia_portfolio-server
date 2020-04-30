from django.shortcuts import render

from django.views.generic import ListView, TemplateView, DetailView
from .models import Artwork

class HomeView(ListView):
    model = Artwork
    template_name = 'home.html'

class ArtworkListView(ListView):
    model = Artwork
    template_name = 'artwork_list.html'

class ArtworkDetailView(DetailView):
    model = Artwork
    template_name = 'artwork_detail.html'




