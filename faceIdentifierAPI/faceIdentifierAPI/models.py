from django.db import models
from django import forms

from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.title