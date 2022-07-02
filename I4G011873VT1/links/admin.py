from django.contrib import admin
from os import link

# Register your models here.
from .models import Link
admin.site.register(Link)
