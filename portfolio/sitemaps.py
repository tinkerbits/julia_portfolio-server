#This exists in order to serve a sitemap at domain.com/sitemap.xml. You can find the full tutorial for it here: https://djangocentral.com/creating-sitemaps-in-django/

from django.contrib.sitemaps import Sitemap
from .models import Artwork

class ArtworkSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Artwork.objects.all()

    def lastmod(self, obj):
        return obj.updated_dt