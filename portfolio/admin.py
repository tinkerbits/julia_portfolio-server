from django.contrib import admin
from .models import Artwork, About, Message

# Register your models here.

class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'hero')

class AboutAdmin(admin.ModelAdmin):
    list_display = ('uploaddate', 'about_photo_name', 'about_text_summary', 'current_photo')

    def about_text_summary(self, obj): #this shortens the about_text value in the Admin list_display to the first 75 characters
        if len(obj.about_text) > 75:
            return ('%s' % (obj.about_text)[:75]+'... (etc.)')
        else:
            return obj.about_text

class MessageAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'email', 'message_summary')

    def message_summary(self, obj):
        if len(obj.message) > 75:
            return ('%s' % (obj.message)[:75]+'... (etc.)')
        else:
            return obj.message




admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Message, MessageAdmin)