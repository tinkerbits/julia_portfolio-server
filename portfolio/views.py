
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from .models import Artwork, About, Message
#from django.shortcuts import render #still needed?
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist




class HomeView(ListView):
    model = Artwork
    template_name = 'home.html'
    queryset = Artwork.objects.filter(Q(hero='left') | Q(hero='middle') | Q(hero='right')).order_by('hero') #orders the hero images on the home page

class ArtworkListView(ListView):
    model = Artwork
    template_name = 'artwork_list.html'
    queryset = Artwork.objects.order_by('-id')


class ArtworkDetailView(DetailView):
    model = Artwork
    template_name = 'artwork_detail.html'

    '''The next two custom methods are to provide links at the end of the lightbox in the ArtworkDetailView. See https://stackoverflow.com/questions/62010753/django-how-get-last-item-from-queryset-in-template/62010798#62010798 for more detail.'''
    def earliest_artwork(self):
        return Artwork.objects.earliest('id')

    def latest_artwork(self):
        return Artwork.objects.latest('id')

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
