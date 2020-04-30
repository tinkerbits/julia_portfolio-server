from django.contrib import admin
from .models import Artwork

# Register your models here.

class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'hero')

admin.site.register(Artwork, ArtworkAdmin)