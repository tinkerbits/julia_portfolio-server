
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from .models import Artwork, About, Message
#from django.shortcuts import render #still needed?
from django.db.models import Q


class HomeView(ListView):
    model = Artwork
    template_name = 'home.html'
    queryset = Artwork.objects.filter(Q(hero='left') | Q(hero='middle') | Q(hero='right')).order_by('hero') #orders the hero images on the home page

class ArtworkListView(ListView):
    model = Artwork
    template_name = 'artwork_list.html'

class ArtworkDetailView(DetailView):
    model = Artwork
    template_name = 'artwork_detail.html'

class AboutView(ListView):
    model = About
    template_name = 'about.html'
    queryset = About.objects.filter(Q(current_photo='enabled'))

class ContactView(CreateView):
    fields = ['name', 'email', 'message']
    model = Message
    template_name = 'contact.html'
    success_url = '/success/'

class ContactSuccessView(TemplateView):
    template_name = 'contact-success.html'
