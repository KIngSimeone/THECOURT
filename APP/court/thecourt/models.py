from django.db import models
from phone_field import PhoneField

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = PhoneField(blank=True, help_text='Contct phone number')

class chat(models.Model):
    chats = models.CharField(max_length=2000)
    pub_time = models.DateTimeField('time published')
