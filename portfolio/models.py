from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Artwork(models.Model):
    date = models.DateField(auto_now_add=True)
    art = models.ImageField(upload_to='artworks/%Y')
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    herochoices = [('left', 'left'), ('middle', 'middle'), ('right', 'right')]
    hero = models.CharField(choices=herochoices, max_length=6, null=True, blank=True, unique=True, error_messages={'unique':'Another artwork already uses this hero position.'})  
    slug = slugify(title, allow_unicode=False)

    def __str__(self):
        return self.title

    def get_absolute_urls(self):
        return reverse('artwork_list', kwargs={'slug': self.slug})


class About(models.Model):
    uploaddate = models.DateField(auto_now_add=True)
    about_photo = models.ImageField(upload_to='about/%Y', null=True, blank=True)
    about_photo_name = models.CharField(max_length=200, null=True, blank=True, unique=True, error_messages={'unique':'Another profile photo with this name already exists.'})
    about_text = models.TextField(null=True, blank=True)
    current_photo_choices = [('enabled', 'enabled')]
    current_photo = models.CharField(choices=current_photo_choices, max_length=7, null=True, blank=True, unique=True, error_messages={'unique':'Another photo is already enabled as about-me photo.'})

    def __str__(self):
        return self.about_photo_name

class Contact(models.Model):
    uploaddate = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    message = models.TextField(null=False, blank=False)