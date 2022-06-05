import imp
from django.contrib import admin
from .models import Teams
from django.utils.html import format_html

# Register your models here.
@admin.register(Teams)
class TeamsAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="50" style="border-radius: 20px" />'.format(object.photo.url))
    
    thumbnail.short_description = 'Photo'
    
    list_display = ['id', 'thumbnail', 'first_name', 'last_name', 'designation', 'created_at']
    list_display_links = ['id', 'thumbnail', 'first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'designation']
    list_filter = ['designation']