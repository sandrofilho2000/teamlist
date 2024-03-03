from django.db import models

class Stadium(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
