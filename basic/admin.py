from atexit import register
from django.contrib import admin

# Register your models here.

from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'description',
                    'category', 'hashtags', 'associates']
