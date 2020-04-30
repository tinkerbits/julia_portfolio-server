from django.db import models
from django.urls import reverse

# Create your models here.

class Artwork(models.Model):

    herochoices = [(1, 'left'), (2, 'center'), (3, 'right')]
    art = models.ImageField(upload_to='artworks/%Y')
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    hero = models.IntegerField(choices=herochoices, unique=True, null=True, blank=True, error_messages={'unique':'Another artwork already uses this hero position.'})  
    
    '''
    def __str__(self):
        #Indicates if an artwork is a frontpager on the admin page
        if self.hero_position == 1:
            template = '{0.title} (hero left)'
        elif self.hero_position == 2:
            template = '{0.title} (hero center)'
        elif self.hero_position == 3:
            template = '{0.title} (hero right)'
        else:
            template = '{0.title}'
        
        return template.format(self)
    '''

    def get_absolute_urls(self):
        return reverse('artwork_list')