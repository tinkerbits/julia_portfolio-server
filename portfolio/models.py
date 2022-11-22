from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save
from slack import WebClient
from django.conf import settings

class Artwork(models.Model):
    created_dt = models.DateField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    # art = models.FileField(upload_to='artworks/%Y')
    art = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    herochoices = [('left', 'left'), ('middle', 'middle'), ('right', 'right')]
    hero = models.CharField(choices=herochoices, max_length=6, null=True, blank=True, unique=True, error_messages={'unique':'Another artwork already uses this hero position.'})  
    slug = models.SlugField(null=True, blank=True, max_length=160, editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('artwork_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    #to save the title as slug (see https://learndjango.com/tutorials/django-slug-tutorial):#
    def save(self, *args, **kwargs): 
        self.slug = slugify(self.title)
        super(Artwork, self).save(*args, **kwargs)


class Message(models.Model):
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name+r"'s message"

# Below is a Django Signal that listens to the save() method being called on the Post model and then sends a message to the Slack API.
def save_post(sender, instance, **kwargs):
    name = instance.name
    email = instance.email
    message = instance.message
    slackbot = WebClient(token=settings.BOT_USER_ACCESS_TOKEN)
    slackbot.chat_postMessage(channel='julia-portfolio', text = f'*<mailto:{email}?body={message}|{name}>* sent a message:\n_{message}_')

post_save.connect(save_post, Message)




