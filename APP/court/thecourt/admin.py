from django.contrib import admin

# Register your models here.
from .models import Players,Chat

admin.site.register(Players)
admin.site.register(Chat)

