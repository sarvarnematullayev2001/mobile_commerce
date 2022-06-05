from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.
@admin.register(Car)
class CarsAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="50" style="border-radius: 15px" />'.format(object.car_photo.url))
    
    thumbnail.short_description = 'Car Image'
    list_display = ['id', 'car_title', 'thumbnail', 'transmission', 'color', 'city', 'model', 'year', 'body_style', 'fuel_type', 'is_featured']
    list_display_links = ['id', 'car_title', 'thumbnail']
    search_fields = ['car_title', 'model', 'body_style', 'fuel_type', 'year', 'transmission']
    list_filter = ['car_title', 'model', 'transmission', 'fuel_type', 'year']
    list_editable = ['is_featured', ]