from django.contrib import admin

# Register your models here.

from app.models import *

class Customization(admin.ModelAdmin):
    list_display = ['sname']

admin.site.register(School,Customization)