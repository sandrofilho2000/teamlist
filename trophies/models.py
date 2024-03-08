from django.db import models


class Trophy(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    
    def __int__(self):
        return self.pk
    
    def __str__(self):
        return self.name

    
