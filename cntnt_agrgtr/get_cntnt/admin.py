from django.contrib import admin

# Register your models here.

from .models import Source, Profile

admin.site.register(Source)
admin.site.register(Profile)