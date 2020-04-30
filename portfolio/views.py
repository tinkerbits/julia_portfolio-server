from django.shortcuts import render

from django.views.generic import ListView, TemplateView
from .models import Artwork

class ArtworkListView(ListView):
    model = Artwork
    template_name = 'artwork_list.html'


class HomeView(ListView):
    model = Artwork
    template_name = 'home.html'

